<!-- topic: reading -->
<!-- sources: gemma4,raschka-ple,scone,engram,quantization,tinyengram,adaptive-input -->

# Reading paths

[简体中文](READING.zh-CN.md)

Choose a question, follow the sources, then check the implementation.

## Before you start

Know how token IDs index a table, how a Transformer block updates the residual stream, and how parameter storage differs from forward-pass computation. For the compression path, familiarity with quantization, bits per value, and host/device memory helps.

## 1. How does PLE work?

Start with the [PLE guide](wiki/ple.md), read Raschka's [architecture explainer](https://www.sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/), then follow `encode_per_layer_input` and `Block.__call__` in [Gemma 4](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py).

Trace the token ID through the table and model-projection branches to the layer's gated residual update. Keep three quantities separate: table parameters, resident memory, and computation per token.

## 2. How do PLE, SCONE, and Engram differ?

Read [contextual n-gram lookup](wiki/ngram-memory.md) alongside the [comparison](COMPARISON.md). Then inspect [SCONE's algorithm](https://arxiv.org/html/2502.01637v3) and the [Engram demo](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py).

Compare the lookup keys, vector construction, injection sites, and training/inference paths. SCONE replaces matched input embeddings with precomputed contextual vectors; Engram's demo adds gated memory at selected internal blocks. PLE supplies layer-specific vectors indexed by token ID.

## 3. What does compression or offloading actually save?

Read the [compression guide](wiki/compression.md), the [input-table quantization example](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_embedding/README.md), and [TinyEngram's systems lab](https://github.com/colorful-lollipop/tinyengram/blob/cf811bef6454dd7a9959b5854af13a52d7ba79f5/docs/lab7-systems.md). Use the [cost matrix](COMPARISON.md#cost-matrix) to organize the result.

Name the object being compressed. Count scales, codebooks, decoders, and buffers alongside the stored values. For offloading, record the transfer volume, cache behavior, bandwidth, and hardware. These determine whether storage savings translate into lower device memory or latency.

For another capacity-allocation design, compare adaptive input's frequency-dependent widths with ALBERT's uniform-width factorization in the [compression guide](wiki/compression.md).

## Read with your own Agent

A useful starting prompt:

> Explain PLE and compare it with SCONE and Engram using this repository and its cited sources. Trace each lookup key to its injection site. Separate parameter storage, device memory, and computation, and identify any missing experimental comparisons. Link the relevant code or paper section for each claim.
