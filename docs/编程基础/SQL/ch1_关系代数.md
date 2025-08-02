# 关系模型

## 是什么

!!! note difinition
    A relation database is a collection of one or more relations, which are based on relational model.A relation is a table with rows and columns.

说白了，relation就是一张表（集合，所以一般不能重复），关系型数据库是表的集合

这里有两个词需要区分：

* relationship:an association among several entities
* relation:the mathematical concept, referred to a table

给定一个集合 $D_1,D_2,...,D_n $，一个关系 $r $就是$D_1 x D_2 x ... x D_n( $D_i$上的笛卡尔积)的一个子集。因此关系就是一个n维元组。

### 属性类型

关系的每项属性都有自己的名称和域，并且属性值必须满足原子性(atomic/indivisible)的。至于什么是原子性，就是不可分，下面是两个反例，它们都不是原子属性：

* 多重属性(multivalued attribute)
* 复合属性(composite attribute)

`null`是一个特殊的值，它存在于任一属性的域中，它不是`''`也不是`0`，它的存在会引发一些问题

### 相关概念

可以这么理解，relation schema是变量的类型，relation instance 是值$A_1,A_2,...,A_n $是属性，$R=(A_1,A_2,...,A_n) $就是一个 relation schema,$r(R) $是在$R $上的关系。一个关系的当前值可以被一张表表示，r的一个元素t就是一个元组(tuple)，可以被表的一行表示。

注意元组的顺序是不相关的(irrelevant)，元组可能以任意顺序储存。在一个关系中元组是不能重复的(no duplicated)

### 键

* 首先，键$K $是关系$R $的属性组合，然后如果$K $可以作为元组的标识（键与元组形成一一映射），那么这个键就是超键(superkey)
* 如果它还是最小的超键(去除任一属性就不再是超键)，那么它就是候选键(candidate key)，注意候选键可以有多个，但它们的元素个数未必相同
* 可以人为指定一个候选键为主键(primary key)，用下划线标示
* 假设存在关系$r(A,B,C) $和$s(B,D) $，且$B $在$s $中是主键，可以说$B $在$r $中是一个外键指向(referencing)$s $，即指向主键。$r $是参照关系，$s $是被参照关系。外键的作用是引入外键约束，以及把两张表关联起来。

### 关系代数

#### 1. 选择

一行一行的去挑

**Notation:**:$\sigma_p (r) $，p叫做选择条件(selection predicate)，表示$\sigma_p(r)=\{t|t\in r $  and  $p(t)\} $，其中 $p(t)$是命题演算(propositional calculus)，包含terms 被 $\land$(and), $\lor$(or), $\neg$(not)连接terms，每个term是`<attribute> op <attribute>`或者常数，其中`op`是 $=,\neq,>,\geq,<,\leq $

#### 2. 投影

一列一列地去挑

**Notation:**$\Pi_{A_1,A_2,...,A_k}(r) $，其中$A_1,A_2,...,A_k $是属性名，$r $是一个关系。结果是k列除去没有选择的列以及去除重复行

#### 3. 并

两张元素兼容的表上下拼接

**Notation:**$r\cup s $，表示 $r\cup s=\{t|t\in r$ or $t \in s \} $，对于操作对象有一定要求：

1. r,s必须等目(same arity)，即有相同数量的属性
2. 属性的名字可以不一样，但是域必须是兼容的

#### 4. 差

一张表扣除另一张表中包含的自己的元素

**Notation:**$r-s $，表示$r-s=\{t|t\in r and t\notin s \} $，要求和“并”一样

#### 5. 笛卡尔积

把两张表的元组全排列

**Notation:**$r\times s $，表示$r\times s=\{\{t q\}t\in r and q\in s \} $。如果r和s的属性名称是不相交的，则正常组合就好，但是如果不是，就需要考虑重命名来避免命名冲突

#### 6. 重命名

一是给关系代数运算的结果命名，二是给元素取别名，格式是$\rho_{\times(A_1,A_2,...,A_n)}(E) $，对E及其attributes都重命名

---

#### 1. 交

参考“并”，**Notation:**:$r\cap s $，表示 $r\cap s=\{t|t\in r$ and $t \in s \} $，实际上 $r\cap s = r - (r - s) $

#### 2. 自然连接

**Notation:** 这个操作要与"并"区分，"并"是接在下面，然连接是找到同名属性相等的元组，然后连接二个关系中 **同名属性值相等**的元组并消除同名属性

Theta join 可以由用户自定义条件$\theta $

#### 3. 除

这个比较抽象，建议结合基本运算理解：

$$R=\{A_1,..,A_m,B_1,..,B_n\} $$

$$S=\{B_1,..,B_n\} $$

$$R-S=\{A_1,...,A_m\} $$

$$R\div S=\{t|t\in \Pi_{R-S}(r)\cap\forall u\in S(tu\in R) \} $$

这个式子表示商是先按照列作差，然后商的所有元组与除数的所有元组拼接都能被被除数覆盖

#### 4. 赋值

字面意思，符号是$\leftarrow $

---

#### 1. 广义投影

就是可以在查的时候就对某些列做一些算数运算，比如某一列的值乘二，或者某一列的值加上另一列的值

#### 2. 聚合函数

求解一系列对象的总体特征，比如总和，平均数，最大值，最小值，总数，符号是$g $，比如 $g_{avg(balance)}(account) $

#### 3. 外连接

扩展自然连接，避免损失信息，比如左连接，就是保证符号左侧的表的数据完整，如果在右侧的表找不到对应的信息则用`null`填充

#### null

null表示未知或者不存在，这里的处理规则就按照SQL：

* null的任何算数运算都是null
* 聚合函数会忽略null
* 比较运算会返回unknow，除非无论null是真是假式子的结果都是确定的

#### 数据库的调整

删除就用减法，插入就用并，更新用广义投影
