<!-- topic: token -->
<!-- sources: weight-tying,gemma4 -->

# Token embeddings

[简体中文](token-embeddings.zh-CN.md) · [README](../README.md) · [Comparison](../COMPARISON.md) · [Sources](../SOURCES.md)

## What is stored?

A token embedding table maps each token ID to a learned vector. For vocabulary size $V$ and hidden width $d$, write the table as $E\in\mathbb{R}^{V\times d}$. Given token $t_i$ at sequence position $i$, the model reads one row:

$$
x_i=E[t_i].
$$

This is a model-internal input representation. It is not a sentence-search service or a retrieval index. A tokenizer determines the IDs and therefore the rows that the model can address.

Gemma 4's `Embedder` provides a clear implementation example. `encode` indexes `input_embedding_table` and scales the result by $\sqrt{d}$. `decode` multiplies each final hidden vector $h_i$ at position $i$ by the transpose of that same table to produce next-token logits. When input and output weights are tied, the model reuses $E$ for both paths:

$$
\text{logits}_i=h_iE^\top.
$$

Weight tying saves a second vocabulary-sized parameter matrix. It does not remove the output projection over the vocabulary: the decoder still needs scores for candidate next tokens. Some architectures use separate input and output tables, so check the model configuration and checkpoint before assuming tying.

## Storage and access

Let $b$ be the number of bits per value. The table's raw vector data uses approximately $Vdb/8$ bytes; this estimate excludes indexes and other metadata. A tied input/output table keeps one copy of those weights. Optimizer states, temporary buffers, quantization scales, padding, and sharding can add storage beyond this estimate. The table is addressed by token ID and normally loaded with model parameters. Moving it to host memory changes transfer and caching requirements; it does not change the mapping itself.

Token embeddings also set the scale of downstream parameterization. Increasing $V$ grows the input table and, when weights are tied, still increases the output vocabulary projection. Rare new rows may receive few training updates.

## How to inspect one

In the [Gemma 4 implementation](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py), inspect `Embedder.setup`, `encode`, and `decode`. Confirm the table shape, the row lookup, the scale, and whether decode uses the same parameter. Then inspect the checkpoint configuration and tensor index. A missing `lm_head.weight` entry can mean that the output head shares storage with the input table; the index alone does not prove that the output head is absent.

This page describes parameter structure and lookup. It does not report an external model run or benchmark. Continue to [PLE](ple.md) for a token-indexed vector at each layer, or [n-gram memory](ngram-memory.md) for lookup keys made from neighboring tokens.
