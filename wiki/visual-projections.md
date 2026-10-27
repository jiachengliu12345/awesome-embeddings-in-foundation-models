<!-- topic: visual-projections -->
<!-- sources: siglip2,gemma4 -->

# Visual projections into model token spaces

[简体中文](visual-projections.zh-CN.md) · [Sources](../SOURCES.md) · [Comparison](../COMPARISON.md)

![Visual modality path: image patches become patch vectors, receive positional vectors, pass through a vision encoder, then are normalized and projected to the language model width.](../assets/modalities.en.svg)

*SigLIP 2 patch projection and Gemma 4 vision-to-language projection are shown as separate paths.*

When an image enters a foundation model, determine whether it looks up a vector, computes one from pixels, or projects a visual representation into another model's width. Here, “projection” means a learned linear mapping, not a discrete vocabulary lookup or a sentence embedding for retrieval.

## From pixels to patch vectors

In the inspected Hugging Face SigLIP 2 implementation, inputs have already been divided into patches and flattened. `Siglip2VisionEmbeddings` applies an `nn.Linear` from $C \times P \times P$ values to the vision hidden width. It then adds a learned positional embedding selected by patch position. The implementation resizes those position embeddings for the input's spatial shape and pads to the requested sequence length. Patch projection computes content from pixel values; positional lookup contributes location information. They are separate parameter objects and operations.

The patch projection multiplies each patch vector by a learned matrix, so work grows with patch count and input dimensions. The positional table scales with its grid; interpolation and padding add runtime work. Higher image resolution can produce more patches and encoder work.

## From vision width to language width

Gemma 4's `encode_vision` applies `mm_pre_projection_norm` with `with_scale=False`, then `mm_input_projection` from `vision_proj_dim` to `embed_dim`. This lets a visual representation enter the language model's token space. The vector is computed by a vision encoder and then transformed; it is not selected by a token ID from a learned vocabulary table. The projection adds learned weights; normalization adds arithmetic without a learned scale in this path. This method is distinct from PLE, which supplies token-indexed, layer-specific vectors inside decoder layers.

Compare visual adapters by input/output width, patch count, projection parameters, normalization, and where vectors are consumed. Record whether the path uses all image patches or selected crops. A linear layer alone does not establish quality or speed; both depend on the encoder, training, resolution, and downstream model.

The [comparison](../COMPARISON.md) separates lookup tables, projections, and decoder injection. Source IDs: `siglip2`, `gemma4` in [SOURCES.md](../SOURCES.md).
