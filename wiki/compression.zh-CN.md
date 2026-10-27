<!-- topic: compression -->
<!-- sources: albert,tensorgpt,optic,quantization,adaptive-input,groupreduce,tt-embedding -->

# 嵌入参数压缩

[English](compression.md) · [来源](../SOURCES.zh-CN.md) · [比较](../COMPARISON.zh-CN.md)

嵌入压缩用更紧凑的参数表示或更低的数值精度存储向量。本页从表的大小出发，介绍低秩分解、自适应维度、张量列分解和量化，并讨论 PLE 的专用压缩。

## 表大小与压缩率

词表大小为 $V$、向量宽度为 $d$ 时，需要存储 $V \times d$ 个标量。若每个标量用 $b$ 位表示，原始表约占 $V \times d \times b / 8$ 字节，尚未计入元数据、对齐空间或优化器状态。压缩率必须注明分母，说明是否计入缩放因子、码本、投影权重、解码器权重和运行时缓冲区。

## ALBERT：低维表与投影

ALBERT 将每个词表示为 $V \times e$ 词表中的一行。在 [`transformer_model()`](https://github.com/google-research/albert/blob/master/modeling.py#L1040-L1100) 中，当 `input_width != hidden_size` 时，代码调用 `dense_layer_2d(..., name="embedding_hidden_mapping_in")`，将嵌入宽度 $e$ 映射到 Transformer 宽度 $d$。因此，查表矩阵和投影矩阵共含 $V \times e + e \times d$ 个权重；只有满足 $Ve+ed<Vd$ 时，权重数才减少。该计数不含投影偏置、位置表、token 类型表、归一化层或 Transformer。查表仍按 token 取一行，投影则为每个 token 增加稠密计算。

## 自适应输入：按词频分配维度

[自适应输入表示](https://arxiv.org/abs/1809.10853v3)为高频与低频词表分组设置不同维度，再投影到统一模型维度。fairseq 的 `AdaptiveInput` 同时存储分组表和投影权重，权重数为 $\sum_g(V_gd_g+d_gd)$，其中 $V_g$ 是第 $g$ 组词数、$d_g$ 是其嵌入维度、$d$ 是公共输出维度。与 ALBERT 的统一低维表相比，它增加了容量分配这一设计轴。`transformer_lm` 共享自适应输入输出权重前会检查分组分界、维度缩减因子和输入输出维度。

## TensorGPT：逐行张量列分解

TensorGPT 将每个 token 的嵌入行分别重塑为张量，并用张量列分解近似表示。推理时，从该行自己的因子中重建所请求的向量。论文 v2 报告了该方法在 GPT 系列模型、其指定任务设置和 Raspberry Pi 上的参数量、任务分数及延迟结果。实际成本取决于因子形状、秩、向量张量化方式和推理内核。

## 输入嵌入量化

LLM Compressor 示例按 `Embedding` 模块选择量化对象，采用对称 INT4 权重、分组缩放因子和 64 的组大小。README 报告 Pythia-1.4B 的结果：Wikitext 困惑度从 FP16 的 14.733 变为 14.752；ARC-Easy 准确率从 0.6048 变为 0.6061。压缩对象还包含量化元数据；推理时需要查找并解包或反量化所需的行。README 配方无需校准数据；若加入校准或与其他权重量化组合，工作流程和比较条件也会改变。

## OPTIC：PLE 压缩

OPTIC 为每个 token 保存一个供多层共享的紧凑码元组，再由对应层的解码器重建该层 PLE 向量。其仓库报告了模型结果，并把压缩率定义为未压缩 BF16 PLE 字节数除以压缩后保留在内存中的字节数。该表示针对 PLE 输出路径进行拟合，改变的是 PLE 的存储形式。

比较方法时，应分别记录总参数、各设备上的常驻字节数、传输字节数、新增投影或解码、FLOPs 和端到端延迟。参数量变少不保证延迟降低：内存访问、查表内核、投影计算、批大小和硬件都可能改变结果。项目统一的成本字段见[比较页](../COMPARISON.zh-CN.md)。

## 分块与整表参数化

[GroupReduce](https://proceedings.neurips.cc/paper_files/paper/2018/hash/a2b8a85a29b2d64ad6f47275bf1360c6-Abstract.html)按词频分组，迭代优化各块的加权低秩近似。[张量化嵌入层](https://aclanthology.org/2020.findings-emnlp.436/)则用共享 TT 因子表示整张表的词表轴与特征轴，并研究端到端训练。两者与逐行压缩 TensorGPT 的对象、共享方式和训练流程不同；应分别核算因子存储与表行重构。

**来源：** [SOURCES.md](../SOURCES.zh-CN.md) 中的 `albert`、`tensorgpt`、`optic`、`quantization`、`adaptive-input`、`groupreduce`、`tt-embedding`。
