# 量子变分算法和PennyLane

[[视频链接]](https://www.bilibili.com/video/BV1Wx4y1N7qd/?spm_id_from=333.337.search-card.all.click&vd_source=26563b4de9f2dd5f6bc6148282be9ca0)

## 1. VQC

需要两个部分：
- 参数化部分 ( $ W_{\theta} $  )
- encoding 部分 ( $ S(x) $  )

<br>
<img src=image.png width=600>
<br>

## 2. 编码方法

<br>
<img src=image-1.png width=600>
<br>

<br>
<img src=image-2.png width=600>
<br>

<br>
<img src=image-3.png width=600>
<br>

<br>
<img src=image-4.png width=600>
<br>

QC-VQC 中使用的是 Time Evolution Encoding

而 Hamiltonian Encoding 一般用于量子本征求解器、量子退火等，这个领域是 Quantum Simulation

## 3. 本教程参考文献

<br>
<img src=image-6.png width=600>
<br>

本文一作为 QML 非常重磅的研究者，写了很多有用的文章和教材

本文讨论的数据编码与 VQC 表达能力的关联

<br>
<img src=image-7.png width=600>
<br>

这篇文章论证了 VQC 可以写成 Fourier series 这种表达形式，用不同层数的 VQC 去拟合傅里叶级数，发现层数越多，拟合效果越好。

<br>
<img src=image-8.png width=600>
<br>
