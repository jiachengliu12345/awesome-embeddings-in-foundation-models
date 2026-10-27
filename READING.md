<!-- topic: reading -->
<!-- sources: gemma4,raschka-ple,scone,engram,quantization,tinyengram,adaptive-input,minbpe,gemma3n-guide,longcat,qwen-ngram,staple,count,memory-layers,groupreduce,tt-embedding,megatron-embedding,tying-bias -->

# Reading guide

[简体中文](READING.zh-CN.md)

The guide begins with language-model input and output representations, then covers layer-wise capacity, contextual lookup, compression, and system costs. Readers familiar with token embeddings can go directly to PLE or n-gram lookup. Vision and audio provide cross-modal comparisons.

## Prerequisites

The foundations assume familiarity with token IDs, matrix multiplication, and Transformer blocks. Compression and systems use low-rank factorization, quantization precision, device memory, and host memory.

## 1. Token embeddings and weight tying

[Karpathy’s tokenization lecture and minbpe](https://github.com/karpathy/minbpe/blob/master/lecture.md) explain how text becomes token IDs; the repository also links to the accompanying video. The [token-embedding guide](wiki/token-embeddings.md) explains how IDs select table rows and how the same matrix can participate in output prediction.

The [weight-tying note](insights/weight-tying.md) connects early experiments, the distributional hypothesis, and recent gradient analysis. The [input/output gradient study](https://arxiv.org/html/2603.26663v1) examines why shared representations align more closely with the output space.

## 2. Per-Layer Embeddings (PLE)

The [Gemma 3n developer guide](https://developers.googleblog.com/introducing-gemma-3n-developer-guide/) introduces the on-device motivation. The [PLE guide](wiki/ple.md) explains layer-wise lookup, model projection, and gated residual updates. In the [Gemma 4 source](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py), `encode_per_layer_input` and `Block.__call__` implement these computations.

[Raschka’s architecture explanation](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/) discusses effective versus total parameters and experimental controls. The [capacity and compute note](insights/capacity-and-compute.md) connects these arguments to formulas and code.

## 3. N-gram lookup and memory layers

The [SCONE and Engram guide](wiki/ngram-memory.md) covers two local-context addressing methods. [SCONE](https://arxiv.org/html/2502.01637v3) reads precomputed input vectors during inference; the [Engram demo](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) illustrates gated memory inside a block. The [mechanism comparison](COMPARISON.md) places PLE, SCONE, and Engram side by side by key and injection site.

Related designs address different questions:

- [LongCat](https://arxiv.org/html/2601.21204v2): capacity allocation between embeddings and MoE experts.
- [Qwen3.8-Next](https://arxiv.org/html/2608.30320v1#S2.SS3): n-gram injection sites, vocabulary budgets, and host prefetching.
- [STAPLE](https://github.com/Infini-AI-Lab/STAPLE): lookup-based residual memory for pretrained checkpoints.
- [COUNT](https://arxiv.org/html/2610.20456v1): n-gram embeddings constructed from corpus statistics and existing output vectors.
- [Memory Layers at Scale](https://github.com/facebookresearch/memory): product-key memory queried by hidden states.

## 4. Compression and systems

The [compression guide](wiki/compression.md) begins with table-storage formulas and covers low-rank factorization, adaptive widths, Tensor Train representations, and quantization. [Adaptive input](https://arxiv.org/abs/1809.10853v3) and [GroupReduce](https://proceedings.neurips.cc/paper_files/paper/2018/hash/a2b8a85a29b2d64ad6f47275bf1360c6-Abstract.html) both group vocabulary by frequency, with different parameterizations and training procedures. [Tensorized Embedding Layers](https://aclanthology.org/2020.findings-emnlp.436/) uses shared TT factors across the whole table, providing a comparison with TensorGPT’s per-row compression.

The [LLM Compressor example](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md) provides an INT4 input-table recipe. The [TinyEngram systems lab](https://github.com/colorful-lollipop/tinyengram/blob/cf811bef6454dd7a9959b5854af13a52d7ba79f5/docs/lab7-systems.md) covers prefetching, caching, and simulated offloading; [Megatron-LM](https://github.com/NVIDIA/Megatron-LM/blob/3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08/megatron/core/tensor_parallel/layers.py#L351) shows vocabulary sharding across devices.

The [cost matrix](COMPARISON.md#cost-matrix) separates parameter storage, device memory, transfer, and computation. Offloading depends on access patterns, bandwidth, and caching; sharding redistributes the per-device load while retaining the table’s total parameter count. The [offline calculator](explorer.html) estimates raw table storage at different shapes and precisions.

## 5. Vision and audio comparisons

The [visual-projection guide](wiki/visual-projections.md) follows image patches through visual representations and projection to language-model width. The [audio-codebook guide](wiki/audio-codebooks.md) covers codec quantization and reconstruction alongside downstream language-model lookup. These topics show how embedding-related components can also produce representations through projection or quantization.

## Agent-assisted reading (optional)

A prompt for an existing coding agent:

> Using this repository and its cited sources, explain the PLE computation path and compare it with SCONE and Engram. Describe each lookup key, stored object, injection site, and computation cost, with code locations or paper sections.
