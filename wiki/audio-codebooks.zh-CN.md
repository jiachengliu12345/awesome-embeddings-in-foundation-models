<!-- topic: audio-codebooks -->
<!-- sources: moshi,cosmos-fsq -->

# 音频码本与语言模型嵌入

[English](audio-codebooks.md) · [来源](../SOURCES.zh-CN.md) · [比较](../COMPARISON.zh-CN.md)

![音频模态路径：编码器量化器将音频特征映射为离散码；码本向量用于重建特征，语言模型再将码 ID 作为 token 输入进行嵌入。](../assets/modalities.zh-CN.svg)

*图注：codec 码本和语言模型中 codec ID 对应的嵌入向量用于不同步骤。Cosmos FSQ 使用固定标量级别，也可以带有可学习投影。*

追踪音频表示经过量化再进入语言模型的过程，并区分 codec 的码本与模型的 token 嵌入表。codec 将连续音频特征转换为离散 ID，并能从离散码重建特征。之后，语言模型可将这些 ID 映射到向量用于预测。两种表或映射可能有不同参数和训练作用。

## Moshi 的 codec 码本

在 Moshi 的 `core_vq.py` 中，`EuclideanCodebook` 将簇使用次数和嵌入向量和存为注册缓冲区。类说明描述了指数移动平均（EMA）；当前质心由嵌入向量和除以簇使用次数得到。因此，这个模块通过 EMA 统计量更新码本，而不是将码本表示为普通的梯度训练嵌入参数。量化时，模型把特征向量分配给质心并输出码 ID；解码时则使用对应的质心向量。若码本大小为 $K$、特征宽度为 $D$，持久状态包含 $K \times D$ 个 EMA 向量和、$K$ 个使用统计及初始化状态。访问质心时，还可能物化一个包含 $K \times D$ 个值的非持久运行时缓存。训练也需要分配和更新计算。

## Moshi 的语言模型查表

`lm.py` 为音频语言模型的每个音频码本创建一个 `ScaledEmbedding` 表，行数为 `card + 1`，宽度为模型维度 `dim`。它还单独创建文本嵌入表和输出投影。这些嵌入表把音频／文本离散 ID 转成供语言模型使用的向量。它们是学习得到的模型参数，与 codec 质心不同。仅音频输入表就有 $n_q \times (card + 1) \times dim$ 个参数，尚未计入文本表、输出头和 Transformer。推理时，查表只是音频 token 预测和生成流程的一部分。

## Cosmos FSQ

Cosmos-Tokenizer 量化器采用有限标量量化（FSQ）：各坐标先限制范围，再四舍五入到固定标量级别，并将这些级别组合为整数索引。它不会为每一种组合码学习一个质心向量。不过，实现仍会将 `implicit_codebook` 物化为非持久缓冲区；若输入宽度与量化器宽度不同，也会使用可学习的 `project_in` 和 `project_out` 线性层。缓冲区和投影各自有存储与运行时成本，需分别计量。

要准确描述成本，先说明讨论的是哪一阶段：codec 编码器／量化器、codec 解码器，还是自回归语言模型。记录码本数量和大小、向量宽度、更新方式、投影层、每秒 ID 数或帧率，以及存储统计是否包括查找表和辅助状态。码率、重建质量、速度与内存占用取决于 codec、帧率、量化器和下游模型。

[比较页](../COMPARISON.zh-CN.md)将码本条目与 token 嵌入行分开记录。来源编号为 [SOURCES.md](../SOURCES.zh-CN.md) 中的 `moshi`、`cosmos-fsq`。
