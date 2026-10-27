<!-- topic: compression -->
<!-- sources: albert,tensorgpt,optic,quantization,adaptive-input,groupreduce,tt-embedding -->

# Compressing embedding parameters

[简体中文](compression.zh-CN.md) · [Sources](../SOURCES.md) · [Comparison](../COMPARISON.md)

Embedding compression stores vectors through a compact parameterization or lower numerical precision. This page introduces low-rank factorization, adaptive widths, Tensor Train representations, and quantization, followed by compression designed for PLE.

## Table size and compression ratio

A vocabulary table with size $V$ and width $d$ stores $V \times d$ scalar parameters. At $b$ bits per value, the raw table takes approximately $V \times d \times b / 8$ bytes, before metadata, alignment, or optimizer states. State whether a compression ratio includes scales, codebooks, projection and decoder weights, and runtime buffers.

## ALBERT: low-dimensional lookup and projection

ALBERT stores each word as a row in a $V \times e$ table. In [`transformer_model()`](https://github.com/google-research/albert/blob/master/modeling.py#L1040-L1100), the code applies `dense_layer_2d(..., name="embedding_hidden_mapping_in")` when `input_width != hidden_size`, mapping the embedding width $e$ to Transformer width $d$. The lookup table and projection matrix therefore use $V \times e + e \times d$ weights. This reduces the weight count only when $Ve+ed<Vd$. This count excludes projection bias, position and token-type tables, normalization, and the Transformer. Lookup still selects a row, while the projection adds a dense operation for each token.

## Adaptive input: frequency-based widths

[Adaptive input representations](https://arxiv.org/abs/1809.10853v3) give frequency-ordered vocabulary bands different widths, then project them to a common model width. fairseq stores both band tables and projections: $\sum_g(V_gd_g+d_gd)$ weights, where $V_g$ is the band size, $d_g$ its embedding width, and $d$ the common output width. This adds a capacity-allocation axis beyond ALBERT’s uniform low-dimensional table. Before tying adaptive input/output weights, `transformer_lm` checks band cutoffs, dimension-reduction factors, and input/output dimensions.

## TensorGPT: per-row Tensor Train decomposition

TensorGPT reshapes and decomposes each token embedding row separately into tensor-train factors. At inference, the requested row is reconstructed from its own factors. Version 2 reports parameter, task-score, and Raspberry Pi latency results for tested GPT-family models. Factor shapes, ranks, vector tensorization, and inference kernels determine actual cost.

## Input-embedding quantization

The LLM Compressor example targets `Embedding` modules with symmetric INT4 weights and group-wise scales (group size 64). Its README reports Pythia-1.4B results: Wikitext perplexity changes from 14.733 (FP16) to 14.752; ARC-Easy accuracy from 0.6048 to 0.6061. Inference must gather and unpack or dequantize rows, and storage includes quantization metadata. The shown recipe is data-free; calibration or combined weight quantization changes the workflow.

## OPTIC: PLE compression

OPTIC shares each token's compact code tuple across layers and reconstructs each layer's PLE vector with its decoder. Its repository reports model results and defines compression as original BF16 PLE bytes divided by compressed resident bytes. The representation is fitted specifically to the PLE output path.

Compare total parameters, per-device resident bytes, transfer volume, added projections or decoding, FLOPs, and end-to-end latency separately. Low parameter count does not guarantee lower latency because memory traffic, kernels, batching, and hardware affect the result. See the [comparison](../COMPARISON.md) for shared cost fields.

## Block and whole-table parameterization

[GroupReduce](https://proceedings.neurips.cc/paper_files/paper/2018/hash/a2b8a85a29b2d64ad6f47275bf1360c6-Abstract.html) partitions by token frequency and refines weighted low-rank approximations within blocks. [Tensorized Embedding Layers](https://aclanthology.org/2020.findings-emnlp.436/) uses shared TT factors across the table’s vocabulary and feature axes and studies end-to-end training. Compare their compressed objects, sharing, and training procedures with TensorGPT’s per-row compression; count factor storage and row reconstruction separately.

**Sources:** `albert`, `tensorgpt`, `optic`, `quantization`, `adaptive-input`, `groupreduce`, `tt-embedding` in [SOURCES.md](../SOURCES.md).
