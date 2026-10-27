# Mechanisms and costs

[简体中文](COMPARISON.zh-CN.md)

Compare the lookup key, stored object, and injection site, then account for storage, access, and computation separately. Read latency alongside the relevant implementation, batch size, and hardware. GB = 10⁹ Bytes; GiB = 2³⁰ Bytes.

| Design | Key / input | Object | Injection | Training |
| --- | --- | --- | --- | --- |
| Token table / tied head | Token ID | E ∈ R^(V×d); same E may supply logits | Before blocks; tied Eᵀ at output | Joint training; tying constrains two roles to one matrix |
| PLE (Gemma 4) | Token ID × layer slice | P ∈ R^(V×L×dₚ), plus projections/gates | Prepared outside blocks; gated update after attention + FFN in each enabled block | Learn table and integration path with model |
| SCONE | Frequent contextual n-gram match | Input contextual vectors; output vocabulary unchanged | Input embedding extension, before backbone | Train separate f-gram learner, then precompute vectors |
| Engram demo | Hashed normalized n-grams, multiple heads | Hashed tables plus key/value projections and convolution | Selected internal blocks, before attention in demo | Learn memory and backbone; released demo mocks backbone parts |
| Factorized embeddings (ALBERT) | Token ID then linear map | V×e lookup and e×d projection | Encoder input | Learn factorized parameterization during training |
| Adaptive input | Token ID in frequency-ordered bands | Band tables V_g×d_g and projections d_g×d | Project selected input row to a common model width | Train variable-capacity input; optional compatible adaptive output tying |
| TensorGPT | Token ID | Per-token tensor-train cores | Reconstruct requested embedding vector | Post-training decomposition without extra training data in paper |
| OPTIC on PLE | Token ID shared across layer decoders | Token code tuples, shared codebooks, per-layer affine decoder | Reconstruct PLE rows before existing integration path | Fit compressed representation against PLE output path |
| Input-table quantization | Token ID | Packed Embedding weights and group scales | Lookup/dequantization at input | Example uses data-free weight-only INT4, group 64 |
| Visual patch / modality projection | Continuous patch or encoder features; positions use IDs | Linear map / convolution; position table is separate | Patch encoder input, or bridge to LM width | Learn projection; training recipe is model-specific |
| Codec codebook / downstream audio table | Codec feature → index; index → LM vector | Codec centroids (Mimi EMA buffers) vs LM embedding parameters | Audio codec quantizer vs downstream LM input | Codec update and LM training are separate roles |
| FSQ contrast | Quantized scalar coordinates ↔ code ID | Fixed levels; optional learned projections and implicit codebook buffer | Image/video codec quantizer | Train surrounding model; centroids are not learned individually |

The [computation-path diagram: token embeddings, PLE, SCONE, and Engram](assets/injection.en.svg) compares their inputs, lookups, and where the vectors are used.

## Cost matrix

| Design | Parameters / ideal storage | Accelerator memory | Access and transfer | FLOPs | Latency |
| --- | --- | --- | --- | --- | --- |
| Token table / tied head | Vd independent values when tied; Vdb/8 Bytes at b bits, excluding extras | Placement dependent; tied head may require broad access to E | Input gathers selected rows; ordinary full logits use all vocabulary rows | Lookup is memory access; full output projection scales with Vd per hidden vector | Not benchmarked |
| PLE (Gemma 4) | Table: VLdₚ values; VLdₚb/8 Bytes; excludes projections | Depends on table placement and materialized layer inputs | Token-addressed rows are predictable; projections and gates still run | Additional model projection and per-layer gate/projection | Not benchmarked |
| SCONE | Cached vector count × width × precision, plus index; training learner separate | Off-accelerator cache in paper; fixed inference accelerator resources under its setup | Match/query/transfer; cache and bandwidth constrain implementation | Learner moved out of inference; training/precompute still cost compute | Query latency reported for the paper’s setup |
| Engram demo | Sum of head-table values × b/8, plus gates/projections; not V×L×dₚ | Predictable addresses permit prefetch design; demo is not a host-offload benchmark | Multiple row reads; collisions and fusion require separate analysis | Hashing, projections, hidden-state-dependent gates, convolution | Not benchmarked |
| Factorized embeddings (ALBERT) | Lookup/projection weights: Ve+ed when e≠d, excluding bias and other tables; reduction requires Ve+ed<Vd. | Depends on table and projection placement | Read e-wide row then project | Adds e→d projection; savings concern storage, not free computation | Not benchmarked |
| Adaptive input | Sum_g(V_g d_g + d_g d) weights, before output sharing and other state | Depends on placement and band/projection temporaries | Band selection, row lookup, projection and output reordering | Band-dependent projection; adaptive output is a separate computation | Not benchmarked |
| TensorGPT | Store tensor-train cores; size depends on factorization and ranks | Core and temporary reconstruction memory depend on runtime | Core access plus reconstruction | Tensor contractions replace direct dense row read | See the paper’s device-specific measurements |
| OPTIC on PLE | Codes + codebooks + layer decoders; denominator must include all | Compact arrays resident; requested rows decoded | Read codes and codebooks, then affine decode | Adds reconstruction; does not remove existing PLE gate/projection | See the repository’s serving measurements |
| Input-table quantization | Vdb/8 packed values + scales, alignment, metadata | Depends on serving kernel; README says packed table stays compact | Gather selected rows plus dequantization | Dequantization added; fused behavior is implementation-specific | Not benchmarked |
| Visual patch / modality projection | Projection m×d (+bias where used); position table separate | Feature activations and image resolution matter | Continuous feature read and matrix multiply | Dense projection; not an ID lookup | Not benchmarked |
| Codec codebook / downstream audio table | Codec K×c per stage; downstream K×d per stream; count separately | Codec state, LM tables, and streaming buffers separate | Codec encode/decode differs from LM token gather | Codec search/decoding vs LM lookup/projection; do not conflate | Not benchmarked |
| FSQ contrast | Fixed grid description ≠ zero allocated codebook buffer | Cosmos implementation materializes implicit_codebook buffer | Scalar quantization and index conversion | May include learned projection; depends on configuration | Not benchmarked |

## Composition evidence

- Implemented: ordinary tied embeddings + PLE + modality projections coexist in Gemma 4's module. [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)
- Implemented: OPTIC reconstructs Gemma 4 PLE rows. [optic](https://github.com/VILA-Lab/optic)
- Implementation documentation: input Embedding quantization may be composed with Linear quantization; verify the actual checkpoint and tied head. [quantization](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md)
- Structural possibility only: PLE + Engram or SCONE + PLE. No matched combination experiment inspected in this edition. [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py), [engram](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py), [scone](https://arxiv.org/html/2502.01637v3)
- Implemented with checks: fairseq ties adaptive input/output weights only with matching partition cutoffs, factors and input/output dimensions. Projection sharing has separate configuration. [adaptive-input](https://arxiv.org/abs/1809.10853v3)

## Evidence by design

- Token table / tied head: [weight-tying](https://aclanthology.org/E17-2025/), [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)
- PLE (Gemma 4): [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py), [gemma3n](https://ai.google.dev/gemma/docs/gemma-3n)
- SCONE: [scone](https://arxiv.org/html/2502.01637v3)
- Engram demo: [engram](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py), [tinyengram](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md)
- Factorized embeddings (ALBERT): [albert](https://github.com/google-research/albert/blob/master/modeling.py)
- Adaptive input: [adaptive-input](https://arxiv.org/abs/1809.10853v3)
- TensorGPT: [tensorgpt](https://arxiv.org/html/2307.00526v2)
- OPTIC on PLE: [optic](https://github.com/VILA-Lab/optic)
- Input-table quantization: [quantization](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md)
- Visual patch / modality projection: [siglip2](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py), [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)
- Codec codebook / downstream audio table: [moshi](https://github.com/kyutai-labs/moshi)
- FSQ contrast: [cosmos-fsq](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py)

[Back to entry](README.md)
