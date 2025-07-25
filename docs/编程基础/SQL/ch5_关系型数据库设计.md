# 关系型数据库设计

## 第一范式

第一范式是原子性，关系型数据库的所有关系都必须满足第一范式，这也是为什么上一章我们需要把phone number这种多值属性划为一个单独的表而不是把它作为一个属性。

如何处理非原子的属性：

* 对于复合属性：拆分成一系列属性
* 对于多值属性：拆分成多个属性，比如phone number拆分成(phone1,phone2,...)，使用一张独立的表

非原子属性的缺陷：

* 存储复杂且重复
* 查询会很麻烦，因为要自行处理
* 插入和删除可能会异常

原子性实际上是域元素使用方式的一种属性，比如字符串通常可以看作是原子的。

!!!note
    为什么我们不把院系和学号混合在一起，比如`CS1001`，这是因为这样存储就不能利用数据库的机制完成查询，比如当我们要查一个计院学生的信息时，就要先把学号查出来，先截取前两位对比出计算机学院的人，再对比编号找到目标。

## 函数依赖

设$\alpha$和$\beta$是$R$的属性，$\alpha\rightarrow \beta$是一个函数依赖当且仅当对于任意两个元组$t_1,t_2$，若$t_1[\alpha]=t_2[\alpha] $，那么$t_1[\beta]=t_2[\beta] $，这个概念借鉴了数学上的函数。

函数依赖本质上是一种一致性约束，表达了一个关系中不同属性的联系。

函数依赖其实是键的泛化：

* K is a super-key for relation schema R if and only if $K\rightarrow R $
* K is a candidate-key if and only if
  * $K\rightarrow R $
  * no $\alpha\in K $，$\alpha\rightarrow R $  

在一个实例上判断函数依赖是容易的，但是在一个关系上是几乎不能做到的，实际逻辑是先给定一个关系函数依赖，再去创建实例

### 平凡的

所谓平凡的(trivial)就是指任何情况下都满足的函数约束，即父集可以决定子集，数学表示为$\alpha\rightarrow \beta $,if$\beta \subseteq \alpha $

### 函数闭包

函数闭包(closure)，当给出一组函数依赖$F $时，有一些依赖关系是隐含在里面的，所有显式和隐式的函数依赖集合就被称作$F $的闭包，记作$F^+ $

### Armstrong’s Axioms

有三条基本公理：

1. 自反律，其实就是平凡的函数依赖，if$\beta\subseteq \alpha $,then$\alpha\rightarrow \beta $
2. 增补律，可以同时增加同一个元组，if$\alpha\rightarrow \beta $,then$\gamma\alpha\rightarrow \gamma\beta $
3. 传递律，if$\alpha\rightarrow \beta , \beta\rightarrow \gamma , $,then$\alpha\rightarrow \gamma $

还有三个推论：

1. 合并律，if$\alpha\rightarrow \beta,\alpha\rightarrow \gamma $,then$\alpha\rightarrow \beta\gamma $
2. 分解律，if$\alpha\rightarrow \beta\gamma $,then$\alpha\rightarrow \beta,\alpha\rightarrow \gamma $
3. 伪传递律，if$\alpha\rightarrow\beta,\gamma\beta\rightarrow \delta $,then$\alpha\gamma\rightarrow \delta $

#### 算法

先使用自反律和增补律，再看有没有可以用传递律的，重复这个过程直到没有新的函数依赖。对于n个元素，总共有$2^n\times 2^n $种可能的函数依赖，这个数字非常大，所以这个算法实际上几乎不可能执行。

#### 属性集的闭包

刚才是函数依赖的闭包，这里定义一个属性$\alpha $的闭包，是可以从给定的F推出的所有$\alpha $单独在箭头左侧的函数依赖的集合

如何判断$\alpha $是不是超键：

1. 先找函数依赖的闭包，然后看$\alpha $的决定的项是否能构成整个关系集
2. 直接找$\alpha $的属性集闭包，在F下由$\alpha $直接或者间接决定的属性集称为$\alpha^+ $

#### 算法

先把$\alpha $纳入结果集result，然后对于F中的关系，如果$\beta\rightarrow \gamma $，并且$\beta $在结果集中，则将$\gamma $纳入结果集，重复这个过程直到结果集没有变化。

#### 属性集闭包的用处

1. 测试超键：看属性集闭包是否包含整个元组
2. 测试函数依赖：看函数依赖是否在属性集闭包中
3. 测试函数依赖闭包：把每个属性的闭包并起来

#### 正则覆盖

如果FD太复杂了，那么检验的开销是很大的，所以我们要尽量减小FD，我们把能够覆盖FD的最小集合叫做正则覆盖，没有任何多余的函数依赖，并且箭头左侧都是unique的

我们需要删除多余属性：

1. 可以被其他依赖隐含的依赖，比如通过传递律
2. 左侧是多余的，比如$\alpha\beta\rightarrow \gamma,\alpha\rightarrow \gamma $
3. 右侧是多余的

#### 实际算法

考虑$\alpha \rightarrow \beta $

如果左边有多余的属性：
计算$(\alpha-A)^+ $是否包含$\beta $

如果右边有多余的属性：
计算$F'=(F-\{\alpha\rightarrow\beta\}\cup \{\alpha\rightarrow(\beta-A)\}) $，看是否包含$\beta $

#### 算法

先使用联合律，再看有没有可以删除的函数依赖，直至没有任何改变

## 分解

在关系型数据库设计中，所有的关系都必须是一种比较好的形式，如果不好则需要分解，分解需要尽量满足：

1. 所有的属性都应该出现
2. 无损全连接分解：分解后的二个子模式的共同属性要么是R1，要么是R2的码。
3. 依赖保持：分解后的每个模式各自的函数依赖闭包合起来可以包含原来的函数依赖闭包
4. 没有重复

### 测试依赖保持

检测$\alpha\rightarrow \beta $是否被保持，对于每一个分解后的元组，计算闭包并添加到结果集中

### BCNF

Boyce–Codd normal form要求一个关系要么是平凡的，要么左侧是分解后关系的超键，BC范式移除了所有的重复。在不分解的情况下，可以直接在F上检验，但是判断分解式则必须在$F^+ $下

### BCNF 分解算法

* 先计算$F^+ $
* 如果有不满足BC范式的关系的$R_i $，找出其中的一个非平凡函数依赖$\alpha\rightarrow\beta $满足$\alpha $是$R_i $的主键，但是$\alpha\rightarrow R_i $不在$F^+ $中，并且$\alpha$和$\beta$有公共部分，那么将$R_i $分解成两个子模式$(\alpha,\beta) $和$R_i-\beta $
* 重复第二步的流程直到没有不满足BC范式的关系

但是实际上不总是能得到同时满足无损全连接和依赖保持的BCNF

### 第三范式

比BCNF弱，允许一些重复，但是还是要依赖保持，第三范式是一定存在的且满足无损全连接和依赖保持的，相比BCNF，第三范式要么是平凡的，要么左侧是超键，要么右侧是主属性，即是某个候选键的一部分

### 第三范式分解算法

* 先求正则覆盖
* 对于正则覆盖里面的每一个函数依赖$\alpha\rightarrow \beta $，如果目前没有关系包含，则添加$(\alpha,\beta) $，重复这个过程直到完全分解
* 如果在所有关系中都不包含候选码则人为添加候选码作为一个关系

### 多值依赖

比如课程、老师和教材，如果一门课对应多名老师，一门课对应多本教材，并且老师和教材没有对应关系，那么老师和教材都满足多值依赖。特别地，函数依赖其实是多值依赖的特殊情况。

多值依赖记作$\alpha\rightarrow\rightarrow \beta $，表示如果$\beta $确定了，那么$\alpha $也就确定了，PPT上的定义异常复杂，看清楚是存在$t_3 $和$t_4 $

这里改用$D^+ $表示多值依赖的全集

### 第四范式

$D^+ $中的所有多值依赖要么是平凡的，要么左侧是超键
