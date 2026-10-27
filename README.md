<a id="top"></a>

# Awesome Embeddings in Foundation Models

[简体中文](README.zh-CN.md)

Curated papers, tutorials, and open-source implementations on embedding mechanisms inside foundation models, for researchers and advanced practitioners. The collection centers on language models: token embeddings, weight tying, Per-Layer Embeddings (PLE), n-gram memory, and embedding compression. Visual projections and audio codebooks provide cross-modal comparisons.

Resources are organized by mechanism, from ordinary token embeddings to designs that add lookup capacity, followed by storage and compute costs. The [research wiki](#wiki) explains the mechanisms, the [comparison](COMPARISON.md) covers lookup keys, injection sites, and costs, and the [reading guide](READING.md) suggests a sequence.

<a id="directory"></a><a id="start-here"></a>

## Contents

- [Token embeddings and weight tying](#category-token)
- [Per-Layer Embeddings](#category-ple)
- [N-gram embeddings and memory layers](#category-memory)
- [Compression and systems](#category-compression)
- [Vision and audio](#category-modalities)
- [Research wiki and comparisons](#wiki)
- [Updates and contributions](#contributing)

<a id="category-token"></a>

## Token embeddings and weight tying

Tokenization assigns IDs to text. An embedding table maps those IDs to vectors; weight tying reuses the input matrix for output prediction. These resources cover the basic computation and the consequences of sharing or allocating embedding parameters.

- [Andrej Karpathy: tokenization and embedding lookup](https://github.com/karpathy/minbpe/blob/master/lecture.md) [![karpathy/minbpe Stars](https://img.shields.io/github/stars/karpathy/minbpe?style=social&label=Stars)](https://github.com/karpathy/minbpe/stargazers)

  Karpathy’s BPE tokenizer implementation and lecture materials connect text, token IDs, vocabulary size, and embedding-table rows.

- [LLMs from Scratch: GPT implementation](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/01_main-chapter-code/gpt.py) [![rasbt/LLMs-from-scratch Stars](https://img.shields.io/github/stars/rasbt/LLMs-from-scratch?style=social&label=Stars)](https://github.com/rasbt/LLMs-from-scratch/stargazers)

  A compact GPT implementation accompanying the book, with token and position embeddings, Transformer blocks, and an output head.

- [Using the Output Embedding to Improve Language Models](https://aclanthology.org/E17-2025/)

  Press and Wolf analyze shared input/output embeddings and report experiments in neural language modeling and machine translation.

- [By Tying Embeddings You Are Assuming the Distributional Hypothesis](https://proceedings.mlr.press/v235/bertolotti24a.html)

  Connects weight tying to the distributional hypothesis and studies when input and output representations support a shared matrix.

- [Weight Tying Biases Token Embeddings Towards the Output Space](https://arxiv.org/html/2603.26663v1)

  Studies input/output gradient imbalance in tied embeddings and interventions that change their alignment with the output space.

<a id="category-ple"></a>

## Per-Layer Embeddings

PLE gives each token a separate learned vector at each decoder layer. The guides explain its role in Gemma; the implementation shows how lookup vectors, projections, and gates form the layer inputs.

- [Google: the Gemma 3n developer guide](https://developers.googleblog.com/introducing-gemma-3n-developer-guide/)

  The model team introduces the on-device motivation for PLE and explains total versus accelerator-resident parameters in Gemma 3n.

- [Gemma 3n: PLE caching](https://ai.google.dev/gemma/docs/gemma-3n)

  Official documentation on PLE caching and accelerator-resident parameters, alongside selective loading of modality parameters in Gemma 3n.

- [Gemma 4 Embedder and block source](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py) [![google-deepmind/gemma Stars](https://img.shields.io/github/stars/google-deepmind/gemma?style=social&label=Stars)](https://github.com/google-deepmind/gemma/stargazers)

  Official embedding and decoder-block code, including token lookup, per-layer projections, gates, weight tying, and modality projections.

- [Per-Layer Embeddings architecture gallery](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/)

  Raschka explains the PLE residual path and discusses baselines needed to separate architectural effects from added parameter capacity.

<a id="category-memory"></a>

## N-gram embeddings and memory layers

Lookup can use a local token sequence or a query derived from hidden states. The designs below differ in their keys, stored vectors, and point of use: SCONE augments input representations, Engram adds gated internal memory, and product-key memory uses hidden-state queries.

- [SCONE: Scaling Embedding Layers in Language Models](https://arxiv.org/html/2502.01637v3)

  Extends input representations with frequent n-grams. A separate model produces contextual vectors that are precomputed for inference lookup.

- [Engram official architecture demo](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) [![deepseek-ai/Engram Stars](https://img.shields.io/github/stars/deepseek-ai/Engram?style=social&label=Stars)](https://github.com/deepseek-ai/Engram/stargazers)

  Architecture demo of n-gram hashing, multi-head lookup, and hidden-state-dependent gating, with simplified attention and MoE components.

- [LongCat: Scaling Embeddings Outperforms Scaling Experts](https://arxiv.org/html/2601.21204v2)

  Compares embedding and MoE capacity allocation and describes the LongCat-Flash-Lite system design.

- [Qwen3.8-Next: n-gram placement and vocabulary ablations](https://arxiv.org/html/2608.30320v1)

  Reports ablations of n-gram injection sites and vocabulary budgets, alongside a host-memory prefetch design.

- [STAPLE: embedding memory for pretrained checkpoints](https://github.com/Infini-AI-Lab/STAPLE) [![Infini-AI-Lab/STAPLE Stars](https://img.shields.io/github/stars/Infini-AI-Lab/STAPLE?style=social&label=Stars)](https://github.com/Infini-AI-Lab/STAPLE/stargazers)

  Adds token-lookup residual memory to pretrained checkpoints, with warm-up and host-offloading designs.

- [COUNT: n-gram embeddings from corpus counts](https://arxiv.org/html/2610.20456v1)

  Constructs n-gram embeddings from fixed corpus statistics and existing output vectors, providing an alternative to learned table rows.

- [Meta: Memory Layers at Scale](https://github.com/facebookresearch/memory) [![facebookresearch/memory Stars](https://img.shields.io/github/stars/facebookresearch/memory?style=social&label=Stars)](https://github.com/facebookresearch/memory/stargazers)

  A comparison with token-ID and n-gram lookup: trainable product-key memory queried by hidden states.

- [TinyEngram systems lab](https://github.com/colorful-lollipop/tinyengram/blob/main/docs/lab7-systems.md) [![colorful-lollipop/tinyengram Stars](https://img.shields.io/github/stars/colorful-lollipop/tinyengram?style=social&label=Stars)](https://github.com/colorful-lollipop/tinyengram/stargazers)

  A systems tutorial on accessed rows, prefetching, caching, and simulated offloading for n-gram memory.

<a id="category-compression"></a>

## Compression and systems

Factorization and quantization reduce the representation cost of a table. Sharding and offloading change where its weights are stored and accessed. This section connects those methods to their reconstruction, communication, and runtime costs.

- [ALBERT factorized embedding source](https://github.com/google-research/albert/blob/master/modeling.py) [![google-research/albert Stars](https://img.shields.io/github/stars/google-research/albert?style=social&label=Stars)](https://github.com/google-research/albert/stargazers)

  Factorizes the vocabulary embedding matrix into a low-dimensional lookup table and a projection to the Transformer hidden width.

- [Adaptive Input Representations](https://arxiv.org/abs/1809.10853v3)

  Assigns different embedding widths to vocabulary groups by frequency, then projects them to a common model width.

- [GroupReduce: frequency-aware low-rank compression](https://proceedings.neurips.cc/paper_files/paper/2018/hash/a2b8a85a29b2d64ad6f47275bf1360c6-Abstract.html)

  Compresses vocabulary blocks with frequency-aware weighted low-rank approximation.

- [Tensorized Embedding Layers](https://aclanthology.org/2020.findings-emnlp.436/)

  Parameterizes an entire embedding table with shared Tensor Train factors and studies end-to-end training.

- [TensorGPT](https://arxiv.org/html/2307.00526v2)

  Compresses individual token vectors with Tensor Train factors and reconstructs a requested vector from its factors.

- [OPTIC: compressed PLE with shared token codes](https://github.com/VILA-Lab/optic) [![VILA-Lab/optic Stars](https://img.shields.io/github/stars/VILA-Lab/optic?style=social&label=Stars)](https://github.com/VILA-Lab/optic/stargazers)

  Compresses PLE with compact token codes shared across layers and layer-specific affine decoders.

- [llm-compressor: input embedding quantization](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md) [![vllm-project/llm-compressor Stars](https://img.shields.io/github/stars/vllm-project/llm-compressor?style=social&label=Stars)](https://github.com/vllm-project/llm-compressor/stargazers)

  An input-embedding quantization recipe using symmetric INT4 weights and group size 64, with reported Pythia-1.4B evaluations.

- [Megatron-LM: vocabulary-parallel embedding lookup](https://github.com/NVIDIA/Megatron-LM/blob/3ddfe0fe07efc73dbdc40d4a02acbc1c1f8a9f08/megatron/core/tensor_parallel/layers.py#L351) [![NVIDIA/Megatron-LM Stars](https://img.shields.io/github/stars/NVIDIA/Megatron-LM?style=social&label=Stars)](https://github.com/NVIDIA/Megatron-LM/stargazers)

  Vocabulary-parallel lookup code: row sharding, token-ID masking, local lookup, and collective communication across devices.

<a id="category-modalities"></a>

## Vision and audio

Visual inputs commonly use learned projections from image patches. Audio models can use both codec codebooks and downstream token embedding tables. These examples show where lookup and projection play different roles across modalities.

- [SigLIP 2 patch and position embeddings](https://github.com/huggingface/transformers/blob/main/src/transformers/models/siglip2/modeling_siglip2.py) [![huggingface/transformers Stars](https://img.shields.io/github/stars/huggingface/transformers?style=social&label=Stars)](https://github.com/huggingface/transformers/stargazers)

  Implementation of image-patch projections and learned position embeddings in the SigLIP 2 vision encoder.

- [Mimi codec and Moshi token embeddings](https://github.com/kyutai-labs/moshi) [![kyutai-labs/moshi Stars](https://img.shields.io/github/stars/kyutai-labs/moshi?style=social&label=Stars)](https://github.com/kyutai-labs/moshi/stargazers)

  Mimi audio codec and Moshi language-model code, showing codec codebooks alongside separate audio token embedding tables.

- [Cosmos Tokenizer: finite scalar quantization](https://github.com/NVIDIA/Cosmos-Tokenizer/blob/main/cosmos_tokenizer/modules/quantizers.py) [![NVIDIA/Cosmos-Tokenizer Stars](https://img.shields.io/github/stars/NVIDIA/Cosmos-Tokenizer?style=social&label=Stars)](https://github.com/NVIDIA/Cosmos-Tokenizer/stargazers)

  Finite Scalar Quantization (FSQ) implementation with fixed scalar levels, optional learned projections, and a materialized codebook buffer.

<a id="wiki"></a>

## Research wiki and comparisons

| Topic | Coverage |
| --- | --- |
| [Token embeddings and weight tying](wiki/token-embeddings.md) | Token IDs, table lookup, and a shared output matrix. |
| [Per-Layer Embeddings](wiki/ple.md) | Layer-specific vectors, projection, and gated residual updates. |
| [SCONE and Engram](wiki/ngram-memory.md) | SCONE input expansion and Engram internal memory. |
| [Embedding compression](wiki/compression.md) | Factorization, quantization, and table-storage accounting. |
| [Visual inputs and modality projections](wiki/visual-projections.md) | Image-patch projections and visual-to-language projections. |
| [Audio codebooks and language-model embeddings](wiki/audio-codebooks.md) | Codec quantization and downstream token embedding tables. |

[Mechanisms and costs](COMPARISON.md) · [Reading guide](READING.md) · [Embedding-table storage calculator](explorer.html)

The calculator opens offline and estimates raw table-weight storage from vocabulary size, width, layer count, and precision.

### Research notes

- [PLE: table capacity and compute cost](insights/capacity-and-compute.md)
- [Weight tying: storage savings and representation constraints](insights/weight-tying.md)

<a id="contributing"></a>

## Updates and contributions

[Update notes](UPDATES.md) · [Full bibliography](SOURCES.md) · [Community discussions](DEMAND.md) · [Glossary](GLOSSARY.md) · [Contribution guide](MAINTENANCE.md)

Maintained by [Jiacheng Liu](https://github.com/jiachengliu12345). Suggestions for papers, tutorials, implementations, and corrections are welcome.

[↑ Back to top](#top)
