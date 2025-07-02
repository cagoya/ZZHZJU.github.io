# 从Java到C#快速上手

C#是一种跨平台的通用语言，是最受欢迎的`.NET`语言，是微软为了替代Java而开发的一门语言，但是这一目的事实上并未实现。C#是一门“很甜”的语言，有非常多的语法糖，这一篇并不会涉及那些“奇奇怪怪”的语法。

## 基础

C#名字里面带C，语法依旧是C/C++-like的，因为是对标的Java，所以事实上特性方面会更像Java

1. C#文件名可以不同于类名
2. `using`关键字用于包含命名空间，一个程序可以包含多个`using`语句
3. C#数据类型：
   1. 值类型
   2. 引用类型：
        * 对象类型：`System.Object`是C#通用类型系统中所有数据类型的终极基类
        * 动态类型：提供了以一种类似于动态语言的语法，用`dynamic`关键字声明，但是一般不推荐使用
   3. 指针类型：同C/C++
4. C#提供了内置的类型转换方法，形如`Toxxx`，这些方法都定义在`System.Convert`类中，失败会抛出`FormatExcption`，除此以外，有`Parse`方法用于将字符串转换成对应数值类型
5. `is`关键字用于判断对象是否为某一类型
6. C# 提供`foreach`语法，形如`foreach(var item in collection)`，`var`表示自动类型匹配，相当于C++的 auto
7. C# 封装访问修饰符多了
   * `internal`：同一个程序集的对象可以访问
   * `protected internal`：访问限于当前程序集或派生自包含类的类型
8. C#引用传参使用`ref`声明引用参数
9. `out`关键字可用于从函数中输出参数给另一个函数
10. C# 提供了一个特殊的数据类型，nullable类型（可空类型），表示在基础值类型范围附加上一个null值，可以用`?`声明可空类型，可以用`??`叫做null合并运算符，如果第一个操作数为null则返回第二个操作数
11. 数组，声明风格同Java
12. 字符串，声明风格同Java,String类有两个属性：`chars`获取`Char`对象的指定位置，`Length`获取String的字符数，常用方法有
    * Compare
    * Contains
    * Substring
13. C# 中结构体并不是类：
    * 可以定义构造函数（只能定义含参的，不含参的是默认的）但是不能定义析构函数  不能继承自或者被继承
    * 结构可以不使用New就实例化，但是如果不使用New，只有在所有字段都被初始化后，字段才会被赋值
    * 结构默认是可变的，有点像JS/Python的类
    * 结构是值类型，默认在栈上
14. 继承写法同C++，有`abstract`，`interface`关键字，不支持多继承，可以用`sealed`禁止被继承，有虚方法，关键字还是`virtual`
15. C# 支持重载运载运算符
16. 预处理器指令，类似于C的宏定义，但并不是宏，主要用途是条件编译

## 进阶

### 特性

特性(Attribute)是一类声明性标签，用于添加元数据，如编译器指令和注释、描述等其他信息，和Java的注解用法基本相同

规定特性的语法如下：

```Csharp
[attribute(positional_parameters, name_parameter = value, ...)]
element
```

`.Net`框架提供了三种预定义特性：

* AttributeUsage：描述如何使用一个自定义特性类
* Conditional：标记一个条件方法，其执行依赖于指定的预处理标识符
* Obsolete：标记不应被使用的程序实体，比如过时的旧方法

创建自定义特性，一个新的自定义特性应继承自`System.Attribute`类

### 反射

反射是指程序可以访问、检测和修改它本身状态的一种能力，在C#里面有如下用途，和Java差不多：

* 查看特性信息
* 获取类型信息（如类名、方法名）
* 调用方法或访问属性/字段
* 检查或修改私有成员

C# 中反射的核心类位于`System.Reflection`，核心类和方法有：

* `Type`：可以用`typeof(ClassNmae)`静态获取类型，也可以用`object.GetType()`从实例动态获取类型
* `MethodInfo`、`PropertyInfo`、`FieldInfo`，字面意思
* `Activator`可用于动态创建对象实例

### 属性

属性(property)是类和结构体中用于封装数据的成员，可以看作是字段包装器，通常由`get`和`set`访问器构成，相当于其他语言里面的`get`和`set`方法

C#允许使用自动实现的属性，比如

```Csharp
public class Person{
    public string Name {get; set;}
}
```

### 索引器

索引器允许一个对象像数组一样使用下标方式访问，一维索引器语法如下，可以看到索引器在定义时是没有名称的，但是有`this`关键字

``` csharp
element-type this[int index] //其实没必要非要是整型
{
    get
    {
        // 返回 index 指定的值
    }

    set
    {
        // 设置 index 指定的值
    }
}
```

### 委托

在C#中，委托(Delegate)是一种类型安全的函数指针，它允许将方法作为参数传递给其他方法，所有的委托都派生自`System.Delegate`类，声明委托的语法如下：

```csharp
public delegate <return type> <delegate-name> <parameter list>
```

相同类型的委托可以叠加，这叫做委托的多播，调用多播的委托相当于依次调用了多个函数

C# 提供了几种常见的委托类型：

* `Action`代表不返回值的方法
* `Func`代表返回值的方法
* `Predicate`代表返回布尔值的方法

### 事件

C#事件是一种特殊的委托，用于将特定事件通知发送给订阅者，即允许将一个对象的状态变化通知其他对象，而不需要知道这些对象的细节，其实这个和JS的事件监听很像

事件在类中声明且生成，且通过使用同一个类或其他类中的委托与事件处理程序关联，包含事件的类用于发布事件，被称作发布器，接受事件的类被称作订阅器

### 泛型

集合还是那些，写法也是类似的，都在`System.Collection`中

* 动态数组 ArrayList
* 哈希表 Hashtable

### 匿名方法

* Lambda表达式：C# 里面这么写`(parameters) => { statement; }`
* 匿名方法：通过`delegate`关键字创建委托实例

## 语法备忘

* readonly用于指定只读的字段，表示让这个字段在构造函数执行完之后就不能再修改了
* `ILogger<>`泛型日志接口，可以关联`<>`中的类
* `IEnumerable<T>`是一个接口类型，是所有可以顺序遍历的集合的基类，返回 IEnumerable 比返回数组 [] 更灵活，尤其用于懒加载、分页、流式数据等场景
* 主构造函数：比如`public class ItemController(Service service) : ControllerBase`，可以不在类内定义字段和构造函数
* `num is > 3 and < 7`是一种很特别的写法，相当于`num > 3 && num < 7`
