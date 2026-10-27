# Sources and inspection limits

[简体中文](SOURCES.zh-CN.md)

What to read each source for, who wrote it, and relevant implementation notes. Experimental results retain their authors’ settings; file versions are listed in the details.

## weight-tying

[Using the Output Embedding to Improve Language Models](https://aclanthology.org/E17-2025/) — Ofir Press; Lior Wolf

Press and Wolf analyze shared input/output embeddings and report experiments in neural language modeling and machine translation.

Experiments cover recurrent language models and neural machine translation.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `EACL 2017, E17-2025`.

- [tie](https://github.com/ofirpress/UsingTheOutputEmbedding/blob/master/README.md) · `cc3c7d2750dd396463d8bda0af58d75f82e5c956` · 2026-10-27T01:51:31Z

</details>

## tying-hypothesis

[By Tying Embeddings You Are Assuming the Distributional Hypothesis](https://proceedings.mlr.press/v235/bertolotti24a.html) — Francesco Bertolotti; Walter Cazzola

Connects weight tying to the distributional hypothesis and studies when input and output representations support a shared matrix.

The argument for tying depends on the relationship between semantic similarity and contextual similarity in the data.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `ICML 2024, PMLR235:3584–3610`.


</details>

## gemma3n

[Gemma 3n: PLE caching](https://ai.google.dev/gemma/docs/gemma-3n) — Google

Official documentation on PLE caching and accelerator-resident parameters, alongside selective loading of modality parameters in Gemma 3n.

PLE caching, MatFormer, and modality parameter skipping change different parts of the resource budget.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `English footer: 2025-11-01; Chinese page may differ`.


</details>

## gemma4

[Gemma 4 Embedder and block source](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) — Google DeepMind

Official embedding and decoder-block code, including token lookup, per-layer projections, gates, weight tying, and modality projections.

The module defines table lookup, projection, gating, and modality input. Memory placement is a runtime concern.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `fa50f0358d92302cfd02451cc45ab9f44336c438`.

- [gemma4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) · `fa50f0358d92302cfd02451cc45ab9f44336c438` · 2026-10-27T01:51:31Z
- [gemma-gate](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) · `fa50f0358d92302cfd02451cc45ab9f44336c438` · 2026-10-27T01:51:31Z

</details>

## scone

[SCONE: Scaling Embedding Layers in Language Models](https://arxiv.org/html/2502.01637v3) — Da Yu et al.

Extends input representations with frequent n-grams. A separate model produces contextual vectors that are precomputed for inference lookup.

Training includes an f-gram learner. Inference uses precomputed vectors, with index storage and transfer costs.

<details>
<summary>Versions and files</summary>

First published: 2025-02-03

Accessed 2026-10-27; version: `arXiv:2502.01637v3, 2025-10-23`.


</details>

## engram

[Engram official architecture demo](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) — DeepSeek-AI

Architecture demo of n-gram hashing, multi-head lookup, and hidden-state-dependent gating, with simplified attention and MoE components.

Architecture demo: attention, MoE, and hyper-connections are omitted or mocked.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `f3ce993dee7c6b2e89c102f367f777926dba016e`.

- [engram](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) · `f3ce993dee7c6b2e89c102f367f777926dba016e` · 2026-10-27T01:51:31Z
- [engram-gate](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) · `f3ce993dee7c6b2e89c102f367f777926dba016e` · 2026-10-27T01:51:31Z

</details>

## albert

[ALBERT factorized embedding source](https://github.com/google-research/albert/blob/master/modeling.py) — Google Research

Factorizes the vocabulary embedding matrix into a low-dimensional lookup table and a projection to the Transformer hidden width.

Encoder reference. A projection maps embedding width to hidden width when they differ.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `be7d9412536c4d751e4fe687e82abc998ec54f46`.

- [embedding_lookup and transformer_model embedding_hidden_mapping_in (lines 1040–1100)](https://github.com/google-research/albert/blob/master/modeling.py) · `be7d9412536c4d751e4fe687e82abc998ec54f46` · 2026-10-27T01:51:31Z

</details>

## tensorgpt

[TensorGPT](https://arxiv.org/html/2307.00526v2) — Mingxue Xu; Yao Lei Xu; Danilo P. Mandic

Compresses individual token vectors with Tensor Train factors and reconstructs a requested vector from its factors.

Each token row is decomposed separately. Factor shapes, ranks, and reconstruction kernels determine its cost.

<details>
<summary>Versions and files</summary>

First published: 2023-07-02

Accessed 2026-10-27; version: `arXiv:2307.00526v2, 2024-10-03`.


</details>

## optic

[OPTIC: compressed PLE with shared token codes](https://github.com/VILA-Lab/optic) — Jiacheng Liu et al.; VILA Lab

Compresses PLE with compact token codes shared across layers and layer-specific affine decoders.

Stores token-shared codes, codebooks, and per-layer decoders. Include all three in compressed storage.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `894852b95d2604c4edd9ebd92e017346481f2e74`.

- [optic](https://github.com/VILA-Lab/optic/blob/main/README.md) · `894852b95d2604c4edd9ebd92e017346481f2e74` · 2026-10-27T01:51:31Z
- [optic-decoder](https://github.com/VILA-Lab/optic/blob/main/src/ple_eval/compact_adapter.py) · `1e2798e0fcc1b79e5a0ae6d3afc6b22c9774b3e6` · 2026-10-27T01:51:31Z

</details>

## quantization

[llm-compressor: input embedding quantization](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md) — vLLM Project contributors

An input-embedding quantization recipe using symmetric INT4 weights and group size 64, with reported Pythia-1.4B evaluations.

The example uses weight-only INT4 with group size 64. Storage includes packed values and quantization scales.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `96227ba7a336a8067aad5b6882092fdc0335a841`.

- [quant](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md) · `96227ba7a336a8067aad5b6882092fdc0335a841` · 2026-10-27T01:51:31Z
- [quant-code](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/llama3_example.py) · `c66f70db7cf784ec9ac7e063d1091e94d7e0c717` · 2026-10-27T01:51:31Z

</details>

## raschka-ple

[Per-Layer Embeddings architecture gallery](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/) — Sebastian Raschka

Raschka explains the PLE residual path and discusses baselines needed to separate architectural effects from added parameter capacity.

Explains the residual path and proposes controlled baselines for isolating the contribution of PLE.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `Live page; no immutable revision exposed`.


</details>

## scratch

[LLMs from Scratch: GPT implementation](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/01_main-chapter-code/gpt.py) — Sebastian Raschka

A compact GPT implementation accompanying the book, with token and position embeddings, Transformer blocks, and an output head.

Chapter 4 shows the token lookup, Transformer stack, and output head in a compact GPT implementation.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `85e37361e911bc98624f0c02f360617bde68b91b`.

- [scratch-code](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/01_main-chapter-code/gpt.py) · `85e37361e911bc98624f0c02f360617bde68b91b` · 2026-10-27T01:51:31Z

</details>

## tinyengram

[TinyEngram systems lab](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md) — TinyEngram contributors

A systems tutorial on accessed rows, prefetching, caching, and simulated offloading for n-gram memory.

The systems lab includes exercises, reference solutions, and offload simulations. Check the assumptions before using its estimates.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `c4fca97a629ae57afb8f21661fd09e9b093b0906`.

- [tiny](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md) · `c4fca97a629ae57afb8f21661fd09e9b093b0906` · 2026-10-27T01:51:31Z

</details>

## siglip2

[SigLIP 2 patch and position embeddings](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py) — Hugging Face contributors

Implementation of image-patch projections and learned position embeddings in the SigLIP 2 vision encoder.

Continuous patch projection and discrete positional lookup are separate operations.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `02f5f9629293632ea50587ac1a74afd4871abcd6`.

- [siglip](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py) · `02f5f9629293632ea50587ac1a74afd4871abcd6` · 2026-10-27T01:51:31Z

</details>

## moshi

[Mimi codec and Moshi token embeddings](https://github.com/kyutai-labs/moshi) — Kyutai contributors

Mimi audio codec and Moshi language-model code, showing codec codebooks alongside separate audio token embedding tables.

Codec EMA state and downstream token tables have separate storage and training roles.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `746036e1d100e397936a629da012d00b87dfc619`.

- [mimi](https://github.com/kyutai-labs/moshi/blob/main/moshi/moshi/quantization/core_vq.py) · `746036e1d100e397936a629da012d00b87dfc619` · 2026-10-27T01:51:31Z
- [moshi-lm](https://github.com/kyutai-labs/moshi/blob/main/moshi/moshi/models/lm.py) · `209b7a59c9c086810a81a7d8b99c5233a0ad87ff` · 2026-10-27T01:51:31Z

</details>

## cosmos-fsq

[Cosmos Tokenizer: finite scalar quantization](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py) — NVIDIA contributors

Finite Scalar Quantization (FSQ) implementation with fixed scalar levels, optional learned projections, and a materialized codebook buffer.

Archived implementation of fixed scalar levels, optional learned projections, and a non-persistent codebook buffer.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `38042e989f236d97736052c4a619619b636db19d`.

- [fsq](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py) · `38042e989f236d97736052c4a619619b636db19d` · 2026-10-27T01:51:31Z

</details>

## adaptive-input

[Adaptive Input Representations](https://arxiv.org/abs/1809.10853v3) — Alexei Baevski; Michael Auli; fairseq contributors

Assigns different embedding widths to vocabulary groups by frequency, then projects them to a common model width.

Frequency bands have different widths. Adaptive input/output tying requires matching cutoffs, factors, and dimensions.

<details>
<summary>Versions and files</summary>

First published: 2018-09-28

Accessed 2026-10-27; version: `arXiv:1809.10853v3 (2019-02-22); file SHAs below`.

- [AdaptiveInput.__init__, weights_for_band, forward](https://github.com/facebookresearch/fairseq/blob/main/fairseq/modules/adaptive_input.py) · `01ac4accaccc3e4625ee2ca6a17cf88df1db0ca1` · 2026-10-27T02:03:11Z
- [build_model tie_adaptive_weights assertions](https://github.com/facebookresearch/fairseq/blob/main/fairseq/models/transformer_lm.py) · `1e3aa72d38a9970916f3677bb3b7871aceaeafce` · 2026-10-27T02:03:11Z
- [Sections 1–3, frequency bands and weight sharing](https://arxiv.org/pdf/1809.10853) · `arXiv:1809.10853v3` · 2026-10-27T02:03:11Z

</details>

## minbpe

[Andrej Karpathy: tokenization and embedding lookup](https://github.com/karpathy/minbpe/blob/master/lecture.md) — Andrej Karpathy

Karpathy’s BPE tokenizer implementation and lecture materials connect text, token IDs, vocabulary size, and embedding-table rows.

The written lecture is partial. It covers the tokenizer-to-table boundary; the linked video and repository continue the BPE lesson.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `file blob ebe169f837d5b0113b7545fcda1db6dd040a1f7d`.

- [Character-level tokenization; trainable table rows; BPE introduction](https://github.com/karpathy/minbpe/blob/master/lecture.md) · `ebe169f837d5b0113b7545fcda1db6dd040a1f7d` · 2026-10-27T05:26:45.040244Z

</details>

## gemma3n-guide

[Google: the Gemma 3n developer guide](https://developers.googleblog.com/introducing-gemma-3n-developer-guide/) — Omar Sanseviero; Ian Ballantyne

The model team introduces the on-device motivation for PLE and explains total versus accelerator-resident parameters in Gemma 3n.

An introductory companion to the technical documentation. The PLE section explains CPU placement in the on-device model design.

<details>
<summary>Versions and files</summary>

First published: 2025-06-26

Accessed 2026-10-27; version: `Developer blog, 2025-06-26; live page`.

- [Per-Layer Embeddings (PLE): Unlocking more memory efficiency](https://developers.googleblog.com/introducing-gemma-3n-developer-guide/) · `Developer blog, 2025-06-26; live page` · 2026-10-27T05:26:45.040244Z

</details>

## longcat

[LongCat: Scaling Embeddings Outperforms Scaling Experts](https://arxiv.org/html/2601.21204v2) — Hong Liu et al.

Compares embedding and MoE capacity allocation and describes the LongCat-Flash-Lite system design.

The claimed advantage holds in the paper’s studied regimes. Read its parameter budgets, model widths, and systems optimizations together.

<details>
<summary>Versions and files</summary>

First published: 2026-01-29

Accessed 2026-10-27; version: `arXiv:2601.21204v2, 2026-02-11`.

- [Architecture, embedding/expert allocation experiments, and systems optimizations](https://arxiv.org/html/2601.21204v2) · `arXiv:2601.21204v2, 2026-02-11` · 2026-10-27T05:26:45.040244Z

</details>

## qwen-ngram

[Qwen3.8-Next: n-gram placement and vocabulary ablations](https://arxiv.org/html/2608.30320v1) — Qwen Team

Reports ablations of n-gram injection sites and vocabulary budgets, alongside a host-memory prefetch design.

Section 2.3 compares injection sites and vocabulary budgets. In its added-capacity experiments, loss falls while some downstream scores saturate or fluctuate.

<details>
<summary>Versions and files</summary>

First published: 2026-08-31

Accessed 2026-10-27; version: `arXiv:2608.30320v1`.

- [Section 2.3; Tables 7–9; host prefetch at Layer 2](https://arxiv.org/html/2608.30320v1) · `arXiv:2608.30320v1` · 2026-10-27T05:26:45.040244Z

</details>

## staple

[STAPLE: embedding memory for pretrained checkpoints](https://github.com/Infini-AI-Lab/STAPLE) — Ranajoy Sadhukhan et al.

Adds token-lookup residual memory to pretrained checkpoints, with warm-up and host-offloading designs.

Retains the pretrained FFN up-projection and adds a token-indexed residual path. The paper specifies cache and serving conditions; the README gives an eight-GPU training workflow.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `arXiv:2610.12599v1; README blob 7e3384be54f7bb02771e9cbd0df14f0870faf68f`.

- [README quick start; paper Sections 2, 8–9](https://arxiv.org/html/2610.12599v1) · `arXiv:2610.12599v1` · 2026-10-27T05:26:45.040244Z
- [Quick start and model variants](https://github.com/Infini-AI-Lab/STAPLE/blob/main/README.md) · `7e3384be54f7bb02771e9cbd0df14f0870faf68f` · 2026-10-27T05:26:45.040244Z

</details>

## count

[COUNT: n-gram embeddings from corpus counts](https://arxiv.org/html/2610.20456v1) — Ian Magnusson; Noah A. Smith; Pang Wei Koh

Constructs n-gram embeddings from fixed corpus statistics and existing output vectors, providing an alternative to learned table rows.

COUNT stores counts on the host and combines existing output embeddings. The paper also studies swapping domain-specific count tables at inference.

<details>
<summary>Versions and files</summary>

First published: 2026-10-14

Accessed 2026-10-27; version: `arXiv:2610.20456v1`.

- [Sections 2.2–2.3 and 5–6](https://arxiv.org/html/2610.20456v1) · `arXiv:2610.20456v1` · 2026-10-27T05:26:45.040244Z

</details>

## memory-layers

[Meta: Memory Layers at Scale](https://github.com/facebookresearch/memory) — Vincent-Pierre Berges; Barlas Oğuz et al.

A comparison with token-ID and n-gram lookup: trainable product-key memory queried by hidden states.

A neighboring mechanism: queries depend on hidden states. The paper and reference implementation discuss sparse lookup, memory bandwidth, and distributed value tables.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `arXiv:2412.09764v1; README blob 4e142638886df2901996d7d77eabd914e8c963ae`.

- [Paper Sections 1, 3, 6; README project overview](https://arxiv.org/html/2412.09764v1) · `arXiv:2412.09764v1` · 2026-10-27T05:26:45.040244Z
- [Project overview and configuration](https://github.com/facebookresearch/memory/blob/main/README.md) · `4e142638886df2901996d7d77eabd914e8c963ae` · 2026-10-27T05:26:45.040244Z

</details>

## groupreduce

[GroupReduce: frequency-aware low-rank compression](https://proceedings.neurips.cc/paper_files/paper/2018/hash/a2b8a85a29b2d64ad6f47275bf1360c6-Abstract.html) — Patrick H. Chen; Si Si; Yang Li; Ciprian Chelba; Cho-Jui Hsieh

Compresses vocabulary blocks with frequency-aware weighted low-rank approximation.

Groups vocabulary items by frequency, then refines weighted low-rank blocks. Experiments use historical neural language and translation models.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `NeurIPS 2018 proceedings`.

- [Introduction and Section 3, GroupReduce](https://proceedings.neurips.cc/paper_files/paper/2018/file/a2b8a85a29b2d64ad6f47275bf1360c6-Paper.pdf) · `NeurIPS 2018 proceedings` · 2026-10-27T05:26:45.040244Z

</details>

## tt-embedding

[Tensorized Embedding Layers](https://aclanthology.org/2020.findings-emnlp.436/) — Oleksii Hrinchuk; Valentin Khrulkov; Leyla Mirvakhabova; Elena Orlova; Ivan Oseledets

Parameterizes an entire embedding table with shared Tensor Train factors and studies end-to-end training.

Represents vocabulary and feature axes using shared TT factors and reconstructs requested rows. The paper studies training these compact layers end to end.

<details>
<summary>Versions and files</summary>

First published: 2019-01-30

Accessed 2026-10-27; version: `Findings of EMNLP 2020, pp. 4847–4860; earlier preprint arXiv:1901.10787`.

- [Introduction; TT-matrix and TT-embedding construction](https://aclanthology.org/2020.findings-emnlp.436.pdf) · `Findings of EMNLP 2020, pp. 4847–4860; earlier preprint arXiv:1901.10787` · 2026-10-27T05:26:45.040244Z

</details>

## megatron-embedding

[Megatron-LM: vocabulary-parallel embedding lookup](https://github.com/NVIDIA/Megatron-LM/blob/3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08/megatron/core/tensor_parallel/layers.py#L351) — NVIDIA; Megatron-LM contributors

Vocabulary-parallel lookup code: row sharding, token-ID masking, local lookup, and collective communication across devices.

Shards the table across vocabulary rows. The forward path masks non-local IDs and combines results; sharding and compression solve different storage problems.

<details>
<summary>Versions and files</summary>

Accessed 2026-10-27; version: `commit 3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08`.

- [VocabParallelEmbedding, lines 351 onward](https://github.com/NVIDIA/Megatron-LM/blob/3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08/megatron/core/tensor_parallel/layers.py#L351) · `commit 3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08` · 2026-10-27T05:26:45.040244Z

</details>

## tying-bias

[Weight Tying Biases Token Embeddings Towards the Output Space](https://arxiv.org/html/2603.26663v1) — Antonio Lopardo; Avyukth Harish; Catherine Arnett; Akshat Gupta

Studies input/output gradient imbalance in tied embeddings and interventions that change their alignment with the output space.

The authors rescale input gradients and change embedding alignment, without consistent downstream gains. Some tied/untied model comparisons also differ in training data.

<details>
<summary>Versions and files</summary>

First published: 2026-03-27

Accessed 2026-10-27; version: `arXiv:2603.26663v1`.

- [Sections 3, 4–6; OLMo model/data comparison](https://arxiv.org/html/2603.26663v1) · `arXiv:2603.26663v1` · 2026-10-27T05:26:45.040244Z

</details>

