<!-- topic: ngram -->
<!-- sources: scone,engram,tinyengram -->

# 上下文 n-gram 查表

[English](ngram-memory.md) · [README](../README.zh-CN.md) · [比较](../COMPARISON.zh-CN.md) · [来源](../SOURCES.zh-CN.md)

n-gram 指连续 $n$ 个 token 组成的序列。模型可以用这段局部 token 上下文作为查找键，生成输入表示或内部残差更新。在 SCONE 中，匹配到的 f-gram 表示会替换该位置的普通 token 嵌入；其他设计也可以把取回的向量作为内部残差更新加入模型。这不同于单 token 嵌入表，也不同于注意力中的完整上下文激活序列。短 n-gram 缓存只保存选定的查找向量，不保存每层的完整上下文状态，也不能替代 Transformer。

## SCONE：频繁 n-gram 输入扩展

SCONE 保留原有 token 词表，并加入一组频繁 n-gram，称为 f-gram。令 $\sigma_i$ 表示序列位置 $i$ 上的 token。系统选择一个以该位置结尾、长度不超过最大值 $K$ 的最长匹配 f-gram。按论文算法，$j$ 是所有匹配项中最小的起始位置，因此选中的是最长匹配后缀。若没有匹配，就使用普通 token 嵌入 $\mathcal{T}(\sigma_i)$。训练期间，独立的 f-gram 模型 $\mathcal{A}_{f\text{-}gram}$ 为匹配项生成表示。训练后，系统预先计算选定 f-gram 的表示，并存入推理查找表 $\mathcal{F}$：

$$
e_i=\begin{cases}
\mathcal{T}(\sigma_i), & \text{无 f-gram 匹配时},\\
\mathcal{A}_{f\text{-}gram}(\mathcal{T}(\sigma_j),\ldots,\mathcal{T}(\sigma_i)), & \text{训练且存在匹配时},\\
\mathcal{F}(\sigma_j,\ldots,\sigma_i), & \text{推理且存在匹配时}.
\end{cases}
$$

训练学习器和在线查表是两个不同组件。推理时读取预计算向量，不会为每次请求运行 f-gram 学习器。原有输出词表保持不变，因此这些 f-gram 不会增加下一个 token 的候选类别。

令 $b$ 表示每个值占用的位数。若存储 $N$ 个 f-gram、每个向量维度为 $d$，仅计算向量原始数据时约占 $Ndb/8$ 字节，不含键索引和其他元数据。论文考察了主机内存和基于 NVMe 的存储。只有当键、向量和访问路径都安排在加速器之外时，才会减少加速器驻留存储；主机带宽、缓存和查表延迟仍需考虑。论文的性能结果属于作者报告。

## Engram：选定 block 中的哈希条件记忆

[Engram 官方演示](https://github.com/deepseek-ai/Engram/blob/main/engram_demo_v1.py)从输入 token ID 构造 2-gram 与 3-gram 哈希，从多头嵌入表取向量，再用隐藏状态对投影值进行门控。默认配置选取第 1、15 层。block 会在 attention 之前把 Engram 输出加到隐藏状态上。演示明确把 attention 和 MoE 等部分设为 mock；它展示数据流，不是生产实现，也没有复现模型结果。

检查 tokenizer 与 padding ID 是否一致、表大小和哈希碰撞、选取的层，以及门控的计算路径。SCONE 从选定的频繁 n-gram 集合读取预计算向量；Engram 演示则把上下文哈希到学习得到的表中。两者都按局部 n-gram 寻址，但算法不同。存储和推理条件见[比较页](../COMPARISON.zh-CN.md)。
