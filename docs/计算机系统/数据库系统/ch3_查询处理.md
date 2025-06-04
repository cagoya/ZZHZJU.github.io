# 查询处理
!!!note
   这一章一定要去看 sjl 智云或者 PPT,cl的PPT这一章比sjl不知道少了多少内容（

## 选择
### 线性搜索
扫描整个文件，然后测试是否满足搜索条件，最坏的开销是$b_r*t_T+t_s $，如果是主键的话搜索块平均减少一半，即$(\frac{b_r}{2})t_T+t_s $。线性搜索的优点是在任何条件下都可以用。

### 索引扫描
#### 相等
1. 在主索引上：在主键上相等，开销为$(h_i+1)(t_T+t_S) $
2. 在主索引上：不是在主键上（有重复），开销为$h_i*(t_T+t_S) + t_S + t_T*b $
3. 在二级索引上：在主键上相等，开销为$(h_i + 1)*(t_T + t_S) $
4. 在二级索引上：不是在主键上，开销为$(h_i + m + n)*(t_T + t_S) $

#### 范围
1. 在主索引上：
   1. $\delta_{A\geq V}(r) $，使用索引找到起点，开销和$A_3 $相同
   2. $\delta_{A\leq V}(r) $，不使用索引，直接线性扫描
2. 在二级索引上：
   1. $\delta_{A\geq V}(r) $，叶子节点是有序的，可以选择扫描叶子节点
   2. $\delta_{A\leq V}(r) $，还是扫描叶子节点
   3. 这两种的I/O开销都很大，毕竟实际存储不连续，线性扫描可能会更好

#### 复合选择
1. 合取：
   1. 选择$A_1 $到$A_6 $的一种算法，和合适的条件组合，尽量得到最低开销的$\delta_{\theta_i}(r) $，然后在取出对应记录后检查其余条件
   2. 如果有对应的复合索引就用复合索引
   3. 需要每一个条件都有索引，根据每一个条件去取出来，然后取交集，如果有的没有索引，就在内存中检测
2. 析取：如果都有索引可以用索引然后取并，否则直接线性扫描

## 排序
外部排序，这里是merge sort，假设有$M $个block大小的内存：
1. 创建归并段，应该有$N = \lceil\log_M(b_r)\rceil $
2. 归并
   1. $M > N $，一次归并就可以解决
   2. $M \leq N $，需要多次归并，应该需要$\lceil\log_{M-1}(N)\rceil $轮

* 每个归并轮次和产生归并段都是把所有块，读一次，写一次，但是我们一律不考虑最后一次写，所以block transer的开销为$2b_r\lceil\log_{M-1}(\frac{b_r}{M})\rceil + b_r $
* 在生成归并段时，每个 run 只需要读写分别寻道一次，然后在归并时需要$2b_r $次寻道，所以 seek 的开销为$2\lceil\frac{b_r}{M}\rceil + 2b_r\lceil\log_{M-1}(\frac{b_r}{M})\rceil - b_r $

!!!note 如何简单理解？
    相当于把block变大了，所以现在只有$\lceil\frac{b_r}{b_b}\rceil $个block，内存大小为$\lfloor\frac{M}{b_b}\rfloor $，至于为什么一个向上取整，另一个向下取整，原因是分到最后残存的不足$b_b $大小的块必须当作完整的$b_b $，但是最后残存的不足的内存却是无法使用的。

这个还可以改进，因为这里内存有剩余的话，可以选择在一次性读写多个块($b_b $个)，然后transfer的开销就变为了$2b_r\lceil\log_{\lfloor\frac{M}{b_b}\rfloor-1}(\frac{b_r}{M})\rceil + b_r $，seek的开销变为了$2\lceil\frac{b_r}{M}\rceil + 2\lceil\frac{b_r}{b_b}\rceil\lceil\log_{\frac{M}{b_b}-1}\lfloor(\frac{b_r}{M})\rfloor-\lceil\frac{b_r}{b_b}\rceil $，但是这个$b_b $如何取值完全是个优化问题，需要用数学（或者机器学习）之类的方法解决。

## 连接
这里疑似不考虑写的开销，因为最后满足join出来的tuple数应该都是一样的。

### nested loop join
对于 outer relation的每一个 tuple，都去遍历一次 inner relation 的每一个 tuple
* transfer cost:$n_r*b_s + b_r $
* seek cost:$n_r+b_r $

### block nested loop join
对于 outer relation的每一个 block，对于这个block中的每一个tuple,都去遍历一次 inner relation 的每一个 tuple
* transfer cost:$b_r*b_s + b_r $
* seek cost:$2b_r $

如果内存中可以放下$r $（假设$r $为小的那个），则为最优情况：
* transfer cost:$b_r + b_s $
* seek cost:$2 $

这个有和 merge sort差不多的优化，因为如果可以完全把一个 relation 放到内存中是很好的，如果不行，可以尽量一次多放一些，假设我们内存大小为$M $
* transfer cost:$\lceil\frac{b_r}{M-2}\rceil b_s+b_r $
* seek cost:$2\lceil\frac{b_r}{M-2}\rceil $

### Indexed nested-loop join
用索引找出对应的 tuple，适用于有索引（没有可以建，自底向上的B+树构建开销并不大）并且是等值连接和自然连接的情况，开销为$b_r(t_T+t_S)+n_r*c $，其中$c $是遍历B+树取出对应的所有元组的开销。


### merge join
在 join-atribute 上排序，然后遍历两个排好序的relation，和merge sort的归并很像，也是适用于等值连接和自然连接的情况，假设已经排好序则开销为（注意主需要遍历一次所有block）：
* transfer cost:$b_r + b_s $ 
* seek cost:$\lceil\frac{b_r}{b_b}\rceil + \lceil\frac{b_s}{b_b}\rceil $

但是平分内存其实并不是最优的，seek 的开销实际可以表示为$\lceil\frac{b_r}{x_r}\rceil + \lceil\frac{b_s}{x_s}\rceil(x_r+x_s=M) $（什么均值不等式

hybird merge-join:如果有一个 relation 排好序了，另一个有二级索引，B+树的叶子节点是有序的，但是二级索引物理空间上是不连续的，所以要先和地址连接，然后对地址排序，再去取出真正的值

### hash join
对于 equal-join 和 nartual-join有效，对JoinAttrs使用哈希函数，把JoinAttrs映射到0~n，然后$r $和$s $分别划分成了$r_0 $~$r_n $和$s_0 $~$s_n $

n和h要求能够使每个$s_i $（注意没有要求$r_i $）都能够放进内存，即$n\geq \lceil\frac{b_s}{M}\rceil $，然后合并时只需要$r_i $和$s_i $进行比较就行，通常n被取作$\lceil\frac{b_s}{M}\rceil*f $，其中$f $被称作修正因子。

流程如下：
1. 划分 s，需要留一个block来输出
2. 划分 r
3. 对于每个 i:
   1. 把$s_i $读进内存，然后建一个内存中的哈希索引，这个哈希索引需要使用不同的哈希函数
   2. 从外存中读出$r_i $，对于$r_i $的每一个 tuple 依次去用哈希索引检索匹配的tuple

s 叫做 build input r 叫做 probe input

递归划分，如果 n 比 M还大了则需要递归划分，在划分的时候只能先划分为 M - 1份，然后再用不同的哈希函数划分为 M-1 份，对 r 也做同样的划分，如果$M > \frac{b_s}{M} + 1\approx n $，可以近似估计为$M>\sqrt{b_s} $

哈希索引的开销有点复杂，如果没有递归划分：
* transfer cost:$3(b_r+b_s)+4n_h $，因为划分阶段相当于读写一次r和s，然后build and probe阶段要读一次，但是可能会出现填不满的 block，极端情况下每个分段都会有，即$n_h $份
* seek cost:$2(\lceil\frac{b_r}{b_b}\rceil + \lceil\frac{b_s}{b_b}\rceil) + 2n_h $
如果有递归划分，其实影响的就是划分的次数
