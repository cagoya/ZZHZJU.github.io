# LINQ
LINQ(语言集成查询)是C#的统一查询语法，用于不同源和格式检索数据，用处类似于JDBC，但是用途更广泛，不仅仅可以用于数据库，还可以用于集合，`XML Docs`等。

## 语法
### 表达式
其实还挺简单，就类似于SQL，比如
```csharp
IList<String> stringList = new List<String>(){
    "C++",
    "Java",
    "Python",
    "Csharp"
}

var result1 = from s in stringList
            where s.Contains("C++")
            select s
// 等价于
var result2 = stringList.Where(s => s.Contains("C++"))
```
上面其实给出了两种写法，第一种真的很像SQL查询，另一种改为了使用`lambda`表达式

查询变量的源数据必须是`IEnumerable<T>`或者`IQueryable<T>`集合，查询并不会立即执行，只有当查询变量被遍历时才会真的去执行并返回结果，所以查询变量是可以被多次使用的，比如
``` csharp
// 使用foreach遍历输出
foreach(var r in result)
{
    console.WriteLine(r);
}
// 直接转化成列表
var resList = result.ToList();
```

查询表达式可能会包含多个`from`子句，相当于分层遍历查找，如果是`select`则是查找出满足条件的对象，如果是`group by`那么则是生成按照指定键组织的序列，查询结果也可以用于构造其他对象，包括内置的字符串乃至其它任何自定义类。同`SQL`，有`where`，`join`,`orderby`、`from`、等可选子句，此外比较不同的是可以使用`let`将表达式的结果储存在新的范围变量中，使用`into`创建存储查询的临时标志符，类似于SQL的子查询，子查询语法同样是有的。

### 编写
正如上面所说我们有两种写法，查询语句的写法非常直观，需要注意的是方法语句，熟悉`IEnumerable<T>`就可以知道它并没有`Where`方法，但是在IDE里面编写代码时又确实会有内敛提示，这是因为标准查询运算符是作为扩展方法来实现的，所以当作是`IEnumerable`的方法就好，比如

``` csharp
IEnumerable<int> largeNumbersQuery = numbers2.Where(c => c > 15);
```

可以看到`Where`里面实际上是一个`lambda`表达式（写成箭头函数的形式），返回值是布尔类型，参数是`int`类型（在上面那个例子中），实际上是`T`类型

某些查询方法必须为方法调用，最常见的是返回单一数值的方法，比如`Max`，`Sum`，`Average`等，并且这些返回单一数值的方法会立即执行，因为它们实际上是执行了`foreach`的