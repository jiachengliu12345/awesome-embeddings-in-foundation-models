<!-- topic: insight-tying -->
<!-- sources: weight-tying,tying-hypothesis,gemma4 -->

# 权重共享通过复用嵌入表减少参数

[English](weight-tying.md) · [中文首页](../README.zh-CN.md) · [token 嵌入](../wiki/token-embeddings.zh-CN.md) · [比较页](../COMPARISON.zh-CN.md)

权重共享（weight tying）是一种参数共享设计，它带来有用但有条件的取舍。在常见语言模型中，输入嵌入把 token ID 映射为向量，输出投影则把隐藏状态映射为词表 logits。当两条路径的维度相容时，模型可以复用同一个矩阵。这样能省去第二个词表规模的矩阵，但同一套表示也必须同时承担输入和输出两种作用。

Press 和 Wolf 在 2017 年的研究中主张在神经语言模型中共享权重。他们分析了共享矩阵的更新方式，并报告在若干语言模型设置下困惑度有所下降。对于神经机器翻译，他们报告模型尺寸减少到原来的一半以下，同时没有损害性能。论文实验涉及循环神经语言模型与神经机器翻译。[Press 与 Wolf，EACL 2017](https://aclanthology.org/E17-2025/)

Bertolotti 和 Cazzola 在 2024 年的分析说明，权重共享应被视为一项假设，而不是无条件的默认选择。他们的理论与实验工作将权重共享和分布假说联系起来：语义相近的符号倾向于具有相近的输入嵌入；出现在相似上下文中的符号则倾向于具有相近的输出嵌入。按照他们的分析，只有当数据符合这种关系时，共享才得到支持。这个条件很关键。输入向量表示模型读取某个符号时如何编码它；输出向量表示模型预测该符号时如何为其打分。在一些场景中，两种角色可能一致，在另一些场景中则可能不同。[Bertolotti 与 Cazzola，ICML 2024](https://proceedings.mlr.press/v235/bertolotti24a.html)

Gemma 4 的当前实现说明，读者应核查具体模型的参数化方式，不能只凭惯例推断：它的 `Embedder.decode` 使用 `input_embedding_table` 的转置来计算词表分数。该实现的常规输入与输出解码路径共用此表；PLE 表是独立参数对象。[Gemma 4 官方实现](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)

## 怎样比较

不共享会使用更多参数，但输入与输出路径可以分别调整。权重共享能减少参数存储，却不会自动降低完整词表 logits 的计算成本；推理收益取决于实现方式和实际瓶颈。有效评估应在架构、数据、分词器、优化预算和推理设置一致时比较共享与不共享模型，同时报告质量、参数量、检查点大小、峰值内存和生成延迟。若词表、维度或 token 频率分布不同，也应明确说明。对具体模型和数据，应权衡节省的参数存储和输入输出表示的共享约束。
