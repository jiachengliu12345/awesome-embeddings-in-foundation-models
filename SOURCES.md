# Sources and inspection limits

[简体中文](SOURCES.zh-CN.md)

What to read each source for, who wrote it, and relevant implementation notes. Experimental results retain their authors’ settings; file versions are listed in the details.

## weight-tying

[Using the Output Embedding to Improve Language Models](https://aclanthology.org/E17-2025/) — Ofir Press; Lior Wolf

Understand the shared input/output parameter object and its historical evaluation.

Experiments cover recurrent language models and neural machine translation.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `EACL 2017, E17-2025`.

- [tie](https://github.com/ofirpress/UsingTheOutputEmbedding/blob/master/README.md) · `cc3c7d2750dd396463d8bda0af58d75f82e5c956` · 2026-10-27T01:51:31Z

</details>

## tying-hypothesis

[By Tying Embeddings You Are Assuming the Distributional Hypothesis](https://proceedings.mlr.press/v235/bertolotti24a.html) — Francesco Bertolotti; Walter Cazzola

Read a conditional argument for tying instead of a universal recommendation.

The argument for tying depends on the relationship between semantic similarity and contextual similarity in the data.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `ICML 2024, PMLR235:3584–3610`.


</details>

## gemma3n

[Gemma 3n: PLE caching](https://ai.google.dev/gemma/docs/gemma-3n) — Google

Separate effective parameter load, PLE caching, and modality parameter skipping.

PLE caching, MatFormer, and modality parameter skipping change different parts of the resource budget.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `English footer: 2025-11-01; Chinese page may differ`.


</details>

## gemma4

[Gemma 4 Embedder and block source](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) — Google DeepMind

Trace lookup, model projection, gating, weight tying, and modality projection.

The module defines table lookup, projection, gating, and modality input. Memory placement is a runtime concern.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `fa50f0358d92302cfd02451cc45ab9f44336c438`.

- [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) · `fa50f0358d92302cfd02451cc45ab9f44336c438` · 2026-10-27T01:51:31Z
- [gemma-gate](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) · `fa50f0358d92302cfd02451cc45ab9f44336c438` · 2026-10-27T01:51:31Z

</details>

## scone

[SCONE: Scaling Embedding Layers in Language Models](https://arxiv.org/html/2502.01637v3) — Da Yu et al.

Compare precomputed contextual n-gram inputs with internal per-layer tables.

Training includes an f-gram learner. Inference uses precomputed vectors, with index storage and transfer costs.

<details>
<summary>Versions and files</summary>

First published: 2025-02-03

Accessed 2026-10-27; version: `arXiv:2502.01637v3, 2025-10-23`.


</details>

## engram

[Engram official architecture demo](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) — DeepSeek-AI

Inspect n-gram hashing, multi-head lookup, and hidden-state-dependent fusion.

Architecture demo: attention, MoE, and hyper-connections are omitted or mocked.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `f3ce993dee7c6b2e89c102f367f777926dba016e`.

- [engram](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) · `f3ce993dee7c6b2e89c102f367f777926dba016e` · 2026-10-27T01:51:31Z
- [engram-gate](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) · `f3ce993dee7c6b2e89c102f367f777926dba016e` · 2026-10-27T01:51:31Z

</details>

## albert

[ALBERT factorized embedding source](https://github.com/google-research/albert/blob/master/modeling.py) — Google Research

Distinguish vocabulary width from model hidden width in a factorized design.

Encoder reference. A projection maps embedding width to hidden width when they differ.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `be7d9412536c4d751e4fe687e82abc998ec54f46`.

- [embedding_lookup and transformer_model embedding_hidden_mapping_in (lines 1040–1100)](https://github.com/google-research/albert/blob/master/modeling.py) · `be7d9412536c4d751e4fe687e82abc998ec54f46` · 2026-10-27T01:51:31Z

</details>

## tensorgpt

[TensorGPT](https://arxiv.org/html/2307.00526v2) — Mingxue Xu; Yao Lei Xu; Danilo P. Mandic

Compare tensor-train reconstruction with quantization of table values.

Each token row is decomposed separately. Factor shapes, ranks, and reconstruction kernels determine its cost.

<details>
<summary>Versions and files</summary>

First published: 2023-07-02

Accessed 2026-10-27; version: `arXiv:2307.00526v2, 2024-10-03`.


</details>

## optic

[OPTIC: compressed PLE with shared token codes](https://github.com/VILA-Lab/optic) — Jiacheng Liu et al.; VILA Lab

Inspect a PLE-specific codec: shared token codes and per-layer affine decoders.

Stores token-shared codes, codebooks, and per-layer decoders. Include all three in compressed storage.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `894852b95d2604c4edd9ebd92e017346481f2e74`.

- [optic](https://github.com/VILA-Lab/optic/blob/main/README.md) · `894852b95d2604c4edd9ebd92e017346481f2e74` · 2026-10-27T01:51:31Z
- [optic-decoder](https://github.com/VILA-Lab/optic/blob/main/src/ple_eval/compact_adapter.py) · `1e2798e0fcc1b79e5a0ae6d3afc6b22c9774b3e6` · 2026-10-27T01:51:31Z

</details>

## quantization

[llm-compressor: input embedding quantization](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md) — vLLM Project contributors

Find a concrete nn.Embedding INT4 group-64 recipe and its accounting limits.

The example uses weight-only INT4 with group size 64. Storage includes packed values and quantization scales.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `96227ba7a336a8067aad5b6882092fdc0335a841`.

- [quant](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md) · `96227ba7a336a8067aad5b6882092fdc0335a841` · 2026-10-27T01:51:31Z
- [quant-code](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/llama3_example.py) · `c66f70db7cf784ec9ac7e063d1091e94d7e0c717` · 2026-10-27T01:51:31Z

</details>

## raschka-ple

[Per-Layer Embeddings architecture gallery](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/) — Sebastian Raschka

Follow the PLE residual path and the author's request for controlled baselines.

Explains the residual path and proposes controlled baselines for isolating the contribution of PLE.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `Live page; no immutable revision exposed`.


</details>

## scratch

[LLMs from Scratch: GPT implementation](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/01_main-chapter-code/gpt.py) — Sebastian Raschka

Ground token lookup and output-head shape before studying extra memory paths.

Chapter 4 shows the token lookup, Transformer stack, and output head in a compact GPT implementation.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `85e37361e911bc98624f0c02f360617bde68b91b`.

- [scratch-code](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/01_main-chapter-code/gpt.py) · `85e37361e911bc98624f0c02f360617bde68b91b` · 2026-10-27T01:51:31Z

</details>

## tinyengram

[TinyEngram systems lab](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md) — TinyEngram contributors

Reason about touched rows, prefetching, caching, and simulated offload.

The systems lab includes exercises, reference solutions, and offload simulations. Check the assumptions before using its estimates.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `c4fca97a629ae57afb8f21661fd09e9b093b0906`.

- [tiny](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md) · `c4fca97a629ae57afb8f21661fd09e9b093b0906` · 2026-10-27T01:51:31Z

</details>

## siglip2

[SigLIP 2 patch and position embeddings](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py) — Hugging Face contributors

Identify continuous patch projection separately from a discrete position table.

Continuous patch projection and discrete positional lookup are separate operations.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `02f5f9629293632ea50587ac1a74afd4871abcd6`.

- [siglip](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py) · `02f5f9629293632ea50587ac1a74afd4871abcd6` · 2026-10-27T01:51:31Z

</details>

## moshi

[Mimi codec and Moshi token embeddings](https://github.com/kyutai-labs/moshi) — Kyutai contributors

Separate codec centroids from downstream audio-token embedding tables.

Codec EMA state and downstream token tables have separate storage and training roles.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `746036e1d100e397936a629da012d00b87dfc619`.

- [mimi](https://github.com/kyutai-labs/moshi/blob/main/moshi/moshi/quantization/core_vq.py) · `746036e1d100e397936a629da012d00b87dfc619` · 2026-10-27T01:51:31Z
- [moshi-lm](https://github.com/kyutai-labs/moshi/blob/main/moshi/moshi/models/lm.py) · `209b7a59c9c086810a81a7d8b99c5233a0ad87ff` · 2026-10-27T01:51:31Z

</details>

## cosmos-fsq

[Cosmos Tokenizer: finite scalar quantization](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py) — NVIDIA contributors

See a fixed scalar grid with optional learned projections and a runtime codebook buffer.

Archived implementation of fixed scalar levels, optional learned projections, and a non-persistent codebook buffer.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `38042e989f236d97736052c4a619619b636db19d`.

- [fsq](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py) · `38042e989f236d97736052c4a619619b636db19d` · 2026-10-27T01:51:31Z

</details>

## adaptive-input

[Adaptive Input Representations](https://arxiv.org/abs/1809.10853v3) — Alexei Baevski; Michael Auli; fairseq contributors

Compare variable-width vocabulary bands and check the conditions for tying adaptive input/output weights.

Frequency bands have different widths. Adaptive input/output tying requires matching cutoffs, factors, and dimensions.

<details>
<summary>Versions and files</summary>

First published: 2018-09-28

Accessed 2026-10-27; version: `arXiv:1809.10853v3 (2019-02-22); file SHAs below`.

- [AdaptiveInput.__init__, weights_for_band, forward](https://github.com/facebookresearch/fairseq/blob/main/fairseq/modules/adaptive_input.py) · `01ac4accaccc3e4625ee2ca6a17cf88df1db0ca1` · 2026-10-27T02:03:11Z
- [build_model tie_adaptive_weights assertions](https://github.com/facebookresearch/fairseq/blob/main/fairseq/models/transformer_lm.py) · `1e3aa72d38a9970916f3677bb3b7871aceaeafce` · 2026-10-27T02:03:11Z
- [Sections 1–3, frequency bands and weight sharing](https://arxiv.org/pdf/1809.10853) · `arXiv:1809.10853v3` · 2026-10-27T02:03:11Z

</details>

