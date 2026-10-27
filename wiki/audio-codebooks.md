<!-- topic: audio-codebooks -->
<!-- sources: moshi,cosmos-fsq -->

# Audio codebooks and language-model embeddings

[简体中文](audio-codebooks.zh-CN.md) · [Sources](../SOURCES.md) · [Comparison](../COMPARISON.md)

An audio codec quantizes continuous features into discrete IDs and reconstructs features from those codes. An audio language model treats the IDs as tokens and maps them through separate embedding tables. Moshi implements both steps; Cosmos provides a contrasting quantization mechanism based on fixed scalar levels.

![Audio modality path: an encoder quantizer maps audio features to discrete codes; codebook vectors reconstruct features, while a language model embeds code IDs as token inputs.](../assets/modalities.en.svg)

*Caption: A codec codebook and the language model's embedding for a codec ID serve different steps. Cosmos FSQ uses fixed scalar levels, with optional learned projections.*

## Moshi's codec codebook

In Moshi `core_vq.py`, `EuclideanCodebook` stores cluster usage and embedding sums as registered buffers. Its docstring describes exponential moving averages (EMA), and derives centroids by dividing sums by usage. This module updates the codebook through EMA statistics, not as ordinary gradient-trained embedding parameters. Quantization assigns feature vectors to centroids and returns IDs; decoding retrieves centroid vectors. For codebook size $K$ and feature width $D$, persistent state contains $K \times D$ EMA sums, $K$ usage values, and initialization state. Accessing the centroids can materialize a further $K \times D$ non-persistent runtime cache. Training also requires assignment and update work.

## Moshi's language-model tables

Moshi `lm.py` creates one `ScaledEmbedding` table per audio codebook, with `card + 1` rows and model width `dim`, plus a separate text table and output projection. These learned tables turn discrete IDs into language-model inputs; they are distinct from codec centroids. Audio input tables alone contain $n_q \times (card + 1) \times dim$ parameters, before text, output heads, and Transformer parameters. At inference, row lookup is only one step in audio-token prediction.

## Cosmos FSQ: a fixed-grid comparison

Cosmos-Tokenizer uses finite scalar quantization (FSQ): each coordinate is bounded and rounded to fixed levels, which combine into an integer index. It does not learn a centroid for every possible code. The code still materializes an `implicit_codebook` non-persistent runtime buffer and can use learned `project_in` and `project_out` layers when input and quantizer widths differ. Account for the runtime buffer and optional projections separately.

## Costs and evaluation objects

The codec encoder, quantizer, decoder, and autoregressive language model perform different computations. Codebook count, size, and width determine the scale of tables and auxiliary state; ID or frame rate affects downstream sequence length. Bitrate and reconstruction quality describe codec trade-offs, while token-prediction and generation costs also depend on the language model.

The [comparison](../COMPARISON.md) keeps codebook entries separate from token-embedding rows. Source IDs: `moshi`, `cosmos-fsq` in [SOURCES.md](../SOURCES.md).
