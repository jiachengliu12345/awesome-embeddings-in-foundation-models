<!-- topic: ple -->
<!-- sources: gemma3n,gemma4,raschka-ple -->

# 每层嵌入（Per-Layer Embeddings，PLE）

[English](ple.md) · [README](../README.zh-CN.md) · [比较](../COMPARISON.zh-CN.md) · [来源](../SOURCES.zh-CN.md)

## “每层”指什么？

PLE 是 Per-Layer Embeddings（每层嵌入），不是位置嵌入。每个 token ID 在每个解码器层都有一个学习得到的向量。Gemma 4 官方源码中的表形状为 $[V,L,d_p]$：词表大小 $V$、层数 $L$ 和每层输入维度 $d_p$。对序列位置 $i$ 上的 token $t_i$ 和层 $\ell$，查表为：

$$
p_{i,\ell}=P[t_i,\ell,:].
$$

这张表让模型在不同层拥有按 token 索引的参数。它不会为序列增加位置，也不是 n-gram 缓存。

## 从表项到逐层信号

Gemma 4 不会把查到的表项直接送进 block。`encode_per_layer_input` 先把普通 token 表示 $x_i$ 从隐藏维度 $d$ 投影成每个 token 一个 $[L,d_p]$ 的 packed 输出。第 $\ell$ 层对应的切片把维度 $d$ 投影到 $d_p$；源码会逐层归一化这些切片。随后查出 $p_{i,\ell}$，将其乘以 $\sqrt{d_p}$，并合并两条路径：

$$
q_{i,\ell}=\frac{\operatorname{RMSNorm}(W_\ell x_i)+\sqrt{d_p}\,p_{i,\ell}}{\sqrt{2}}.
$$

其中 $W_\ell$ 表示 packed 投影中第 $\ell$ 层的切片，$q_{i,\ell}$ 是合并后的逐层信号。随后，每个 block 会把自己的输出映射到门控输入，应用 GELU，与该层的 $q_{i,\ell}$ 相乘，再投影回隐藏维度并归一化，最后把结果加到 block 输出上。这构成一条额外残差路径。PLE 表本身是静态学习参数，但 block 使用的信号还取决于普通 token 表示和当前 block 输出。因此，从查表到最终隐藏状态的整条计算并非完全静态。

## 容量与放置

令 $b$ 表示每个值占用的位数。仅计算 PLE 表的向量原始数据时，约占 $VLd_pb/8$ 字节；该估算不含索引和其他元数据。投影、门控、归一化参数、优化器状态和运行时激活还会增加占用。查找会访问某个 token 跨层的向量；实现可能一次生成多层信号，也可能分阶段计算。估算峰值内存前要检查实际运行路径。被检查的源码把表定义为模型参数，但这本身不能证明支持主机卸载，也不能证明节省了多少内存。

## 怎样检查实现

在 [Gemma 4 源码](https://github.com/google-deepmind/gemma/blob/main/gemma/gm/nn/gemma4/_modules.py)中查看 `Embedder.setup`、`encode_per_layer_input` 和 `Block.__call__`。沿着表形状、投影与归一化、token 行查找，再到后续门控和残差相加逐步核对。[Gemma 3n 官方指南](https://ai.google.dev/gemma/docs/gemma-3n?hl=zh-cn#ple-caching)可帮助理解较早的 PLE 接口和缓存说明；不同代际的运行细节不能直接视为相同。

这些来源说明架构，不证明 PLE 在所有设置下都能提升质量或速度。比较条件见[比较页](../COMPARISON.zh-CN.md)；[token 嵌入](token-embeddings.zh-CN.md)介绍单张输入／输出共享表。
