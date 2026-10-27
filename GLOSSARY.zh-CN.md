# 术语表

[English](GLOSSARY.md)

| English | 中文 | 约定 |
| --- | --- | --- |
| embedding | 嵌入 | 写清对象：表、连续表示或投影。 |
| Per-Layer Embeddings (PLE) | 每层嵌入 | 沿用 Google 中文术语；不是位置嵌入。 |
| weight tying | 权重共享 | 输入输出可共用矩阵，不等于所有表共享。 |
| token | token | 保留社区常用写法。 |
| n-gram | n-gram | 由连续 n 个 token 组成的序列。 |
| codebook | 码本 | 说明是 codec 中心、压缩字典、固定网格还是 LM 表。 |
| offloading | 卸载 | 说明主机／设备放置、传输和缓存。 |
| compression ratio | 压缩率 | 原始 Bytes／压缩后 Bytes，写清元数据计量。 |
| FLOPs | 浮点运算次数 | 与 FLOPS（每秒浮点运算次数）区分。 |
| accelerator memory footprint | 加速器内存占用 | 区分驻留权重、激活、缓冲区和缓存。 |
