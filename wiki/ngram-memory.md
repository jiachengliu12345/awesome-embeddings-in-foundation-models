<!-- topic: ngram -->
<!-- sources: scone,engram,tinyengram -->

# Contextual n-gram lookup

[简体中文](ngram-memory.zh-CN.md) · [README](../README.md) · [Comparison](../COMPARISON.md) · [Sources](../SOURCES.md)

An n-gram is a sequence of $n$ consecutive tokens. A model can use local token context as a lookup key for an input representation or an internal residual update. In SCONE, a matched f-gram representation replaces the ordinary token embedding at that position; other designs can add a retrieved vector as an internal residual update. Lookup uses local token combinations; the Transformer then continues to process sequence context through attention.

## SCONE: a frequent n-gram input extension

SCONE keeps the original token vocabulary and adds a set of frequent n-grams, called f-grams. Let $\sigma_i$ be the token at sequence position $i$. The method selects the longest matching f-gram ending there, up to maximum length $K$. In the paper's algorithm, $j$ is the smallest starting position among matches, so the selected f-gram is the longest matching suffix. If there is no match, the model uses the ordinary token embedding $\mathcal{T}(\sigma_i)$. During training, a separate f-gram model $\mathcal{A}_{f\text{-}gram}$ produces the matched representation. After training, the system computes each selected f-gram representation in advance and stores it in an inference lookup $\mathcal{F}$:

$$
e_i=\begin{cases}
\mathcal{T}(\sigma_i), & \text{if no f-gram matches},\\
\mathcal{A}_{f\text{-}gram}(\mathcal{T}(\sigma_j),\ldots,\mathcal{T}(\sigma_i)), & \text{training and a match exists},\\
\mathcal{F}(\sigma_j,\ldots,\sigma_i), & \text{inference and a match exists}.
\end{cases}
$$

The training learner and serving lookup are different components. Inference looks up a precomputed vector; it does not run the f-gram learner for every query. The original output vocabulary remains unchanged, so these f-grams do not add next-token classes.

Let $b$ be the number of bits per value. For $N$ stored f-grams and vector dimension $d$, the vectors' raw data uses approximately $Ndb/8$ bytes, excluding the key index and other metadata. The paper studies main-memory and NVMe-backed stores. Storing precomputed vectors in host memory or on NVMe can reduce their accelerator residency. Key indexes, caches, and temporary buffers contribute storage according to their placement; access costs depend on bandwidth, cache behavior, and lookup latency.

## Engram: hashed conditional memory in selected blocks

The [official Engram demo](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py) constructs 2- and 3-gram hashes from input token IDs, retrieves vectors from multi-head embedding tables, and uses hidden states to gate a projected value. Its default configuration selects layers 1 and 15. The block adds the Engram output before attention. The demo uses mock attention and MoE components to focus on the Engram data flow.

## Design comparison

The tokenizer, padding ID, hash-table sizes, and selected layers determine the concrete lookup and fusion behavior. SCONE uses a selected frequent-gram set with precomputed vectors; Engram's demo hashes contexts into learned tables. They are related by local n-gram addressing, but they are not the same algorithm. See [comparison](../COMPARISON.md) for storage and serving conditions.
