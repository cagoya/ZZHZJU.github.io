# 基础
!!!note
    GO语言集众家之所长，是C系的语言，但是长的又比较与众不同，许多能够在大多数面向对象语言中使用的特性 Go 语言都没有支持

## 简介
GO 被设计成了一门应用于搭载Web服务器，存储集群或者类似用途的巨型中央服务器的编程语言，它提供了海量的并行支持，也是目前大厂，比如bytedancing等转型的方向

emm，大体结构比较像java，最开始使用`packge`要声明包，然后`import`引入库，`func main`是`main`函数的写法，GO不需要像C系语言那样以分号结尾而是一行代表一个语句结束

GO的变量定义写法有点怪，变量类型在后面`var identifier1, identifier2 type`，如果没有初始化那么会有默认值（零值），如果有初始化GO支持自动判断类型，这个还可以进一步简写省略掉`var`，直接用`:=`，这个写法被称为初始化声明，但是只能用于局部变量，注意GO里面定义局部变量但是不使用是非法的，会编译报错，也是有点离谱

GO支持多变量赋值，也可以是多变量初始化声明，GO里面的`_`称为空白标识符，是只写变量，专门用于丢弃值

GO的常量还是用`const`,`iota`表示特殊常量，可以被编译器修改，`iota`在`const`出现时被置为0，每增加一行常量声明都会使`iota`计数+1，可以理解为const语句块的行索引，够可以用成枚举

GO的自增自减都是写在后面，条件语句多了一个`select`，类似于`switch`，但是会随机执行一个可运行case

函数用`func`声明，返回类型也是写在最后面，GO函数可以返回多个值，如同元组，因为GO是有指针的，所以默认都是值传递

声明数组也是反过来的，`var arrayName [size]dataType`，也是有初始化声明的语法的

GO中指针的用法和C差不多，连指针类型的写法都是反的，比如`*int`，空指针是nil，GO虽然提供了指针，但是不允许指针的运算，内存回收也是由解释器完成

GO语言有结构体语法，`type struct_name struct{}`，通过指针访问结构体也是用`.`，而不是`->`

GO提供了切片(slice)，即其他语言里面的动态数组，切片不指定长度，比如`var identifier []type`，或者使用`make()`函数来创建切片`var slice1 []type = make([]type, len)`，这样就可以指定原始长度了，数组有切片语法，但是没有步长，`arr[startIndex:endIndex]`表示一个切片，`len()`返回当前长度，`cap()`返回最大长度，空切片自然也是nil,`append()`增加，`copy()`拷贝，但是它们应该写在前面

GO里面的变量也是`foreach`，但是只有键值对的遍历，比如
```go
// 就连数组也是理解成键值对
// 假设不想读取下标，那么就把下标写成_
var pow = []int{1,2,3,4},
for i, v := range ,pow{
    fmt.Printf(i,v)
}
```

GO的map同C++的map，如果键不存在会返回零值，并不会抛出错误，map是引用类型，map定义方法如下`map_varible := make(map[KeyType]ValueType, initialCapacity)`，删除元素使用`delete()`

GO语言的类型转换风格同C，GO不允许强制类型转换，可以将字符串转化为其他类型，比如
```go
var str string = "10"
var num int
// Atoi 返回两个值，第一个是转换后的整型值，第二个是可能发生的错误，可以使用空白标识符来忽略这个错误
num, _ = strconv.Atoi(str)
```
也可以将整数转化为字符串，使用`strconv.Itoa`

Go 语言没有类和继承的概念，所以它和 Java 或 C++ 看起来并不相同。但是它通过接口（interface）的概念来实现多态性。接口在GO里面是一种类型，定义一个简单的接口：
```go
type Shape interface {
    // 只有返回值类型的函数
    Area() float64
    Perimeter() float64
}
```
任意类型只要实现了这两个方法，就被认为是实现了Shape接口