<!-- topic: ple -->
<!-- sources: gemma3n,gemma4,raschka-ple -->

# Per-Layer Embeddings (PLE)

[简体中文](ple.zh-CN.md) · [README](../README.md) · [Comparison](../COMPARISON.md) · [Sources](../SOURCES.md)

## Parameter structure

Per-Layer Embeddings (PLE) give each token a separate learned vector at each decoder layer. In Gemma 4's official source, the table has shape $[V,L,d_p]$: vocabulary size $V$, number of layers $L$, and per-layer input width $d_p$. For token $t_i$ at sequence position $i$ and layer $\ell$, the lookup is:

$$
p_{i,\ell}=P[t_i,\ell,:].
$$

The token ID and layer index together select a table entry, so the same token can receive a different vector at each layer.

## Computation path

Gemma 4 combines the table lookup with a projection of the ordinary token representation. Its `encode_per_layer_input` first projects the ordinary token representation $x_i$ from hidden width $d$ into a packed output of shape $[L,d_p]$ for each token. The slice for layer $\ell$ is a projection from $d$ to $d_p$; the source normalizes each layer slice. It then looks up $p_{i,\ell}$, scales that vector by $\sqrt{d_p}$, and combines the two branches:

$$
q_{i,\ell}=\frac{\operatorname{RMSNorm}(W_\ell x_i)+\sqrt{d_p}\,p_{i,\ell}}{\sqrt{2}}.
$$

Here $W_\ell$ denotes the layer-$\ell$ slice of the packed projection, and $q_{i,\ell}$ is the combined per-layer signal. In each block, the code maps the block output to a gate input, applies GELU, multiplies by that layer's $q_{i,\ell}$, projects back to hidden width, normalizes, and adds the result to the block output. This is an additional residual path. The table is a static learned parameter, while the signal used by a block also depends on the ordinary token representation and the current block output. The projection and gate combine these stored parameters with the current computation state.

## Capacity and placement

Let $b$ be the number of bits per value. The PLE table's raw vector data uses about $VLd_pb/8$ bytes; this estimate excludes indexes and other metadata. Projection, gate, normalization parameters, optimizer state, and runtime activations add to that figure. Lookup touches one token row across layers; an implementation may materialize several layer signals together or compute them in stages. Check the actual runtime before estimating peak memory. Storage placement and caching determine which parameters reside on the accelerator; the Gemma 3n documentation separately describes PLE caching.

## Implementation reference

In the [Gemma 4 source](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py), inspect `Embedder.setup`, `encode_per_layer_input`, and `Block.__call__`. Follow the table shape, projection and normalization, token-row lookup, and later gate/residual addition. The official [Gemma 3n guide](https://ai.google.dev/gemma/docs/gemma-3n#ple-caching) is useful for the earlier PLE interface and its caching discussion; do not assume identical runtime details across model generations.

The [research note](../insights/capacity-and-compute.md) discusses capacity and compute. See the [comparison](../COMPARISON.md) for cost fields and [token embeddings](token-embeddings.md) for a single shared input/output table.
