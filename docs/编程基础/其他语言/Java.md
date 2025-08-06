# Java

> 这里是站在已经掌握了 C++ 的基础上来学习 Java 的，所以一些完全相同的东西就不再赘述了。

## 简介

Java 最早是针对小型家电设备的嵌入式应用开发而设计的语言，最开始反响平平，但是后来互联网兴起后，Java成为了后端开发的主流语言。Java 介于解释型和编译型语言之间，先将代码编译成一种“字节码”，再由JVM解释执行。

随着Java的发展，Java又分出了三个不同版本：

* Java SE：Standard Edition
* Java EE：Enterprise Edition
* Java ME：Micro Edition

它们之间的包含关系是$\text{ME} \subset \text{EE} \subset \text{SE}$

Java 中常见的缩写解释：

* JVM：Java 虚拟机，相当于一个解释器
* JDK：Java 开发工具包，JRE + 开发工具
* JRE：Java 运行环境，JVM + Java 标准库

## 基础

```java
public class HelloWorld {
    public static void main(String[] args) {
        // 输出 Hello World
        System.out.println("Hello World");
    }
}
```

Java 中所有方法和变量都必须定义在类中，`JVM`默认`main`函数是程序的入口，如果没有运行时会报错。

Java 中的注释有三种：

* `//`：单行注释
* `/* */`：多行注释
* `/** */`：文档注释

Java 代码编译的过程：Java 代码文件的后缀名是`.java`，被Java编译器编译之后编译成`.class`文件，之后在JVM中运行。

### 基础数据类型

Java 中的类型可以分为值类型和引用类型，基础值类型和 C++ 差不多，有：

* 整数类型：`byte`，`short`，`int`，`long`
* 浮点数类型：`float`，`double`
* 字符类型：`char`
* 布尔类型：`boolean`

一些说明：

1. `Java`只定义了带符号的整型
2. Java语言对布尔类型的存储并没有做规定，因为理论上存储布尔类型只需要1 bit，但是通常JVM内部会把`boolean`表示为4字节整数
3. Java的`char`类型除了可表示标准的ASCII外，还可以表示一个Unicode字符，无论中英文都是占两个字节

除了上述基本类型的变量，剩下的都是引用类型，在Java中，引用类型的变量非常类似于C/C++的指针，引用类型指向一个对象，所有引用类型的默认值都是`null`。对于基本类型，Java提供了对应的包装类型，比如`int`对应的包装类型是`Integer`，`Integer`就是一个引用类型，这个主要是为了方便传参。

常量使用`final`关键字定义，也就是`C++`里面的`const`，除此之外`final`还可以用于限制方法和类，限制方法后，该方法不能被重写，限制类后，该类不能被继承。

Java 支持使用`var`来进行自动类型推断，用法同C++的`auto`。

```java
var a = 1;
var b = "Hello";
```

类型转换还是和C++差不多，对于`short + int`这种会自动向上提升为`int`，即隐式类型转换，显式类型转换还是类似于`(int) a`。

### 字符串

`String`是引用类型，Java中的`String`也是支持`+`的（这个只能说是特殊考虑，`Java`其实是不支持运算符重载的），对于非字符串类型，`Java`会自动尝试类型转换。

```java
int a = 5;
String b = "Hello";
String c = a + b; // "5Hello"
```

Java 支持多行字符串，和Python一样是三引号`"""`，此外Java中的字符串同样是不可变的。

这里给出一些常用的方法，基本是如今高级语言都会有的，对于单个字符：

```java
isDigit(ch) // 判断是否为数字
isLetter(ch) // 判断是否为字母
isLetterOrDigit(ch) // 判断是否为字母或数字
toLowerCase(ch) // 转换为小写
toUpperCase(ch) // 转换为大写
isLowerCase(ch) // 判断是否为小写
isUpperCase(ch) // 判断是否为大写
```

对于字符串：

```java
length() // 获取长度
isEmpty() // 判断是否为空
isBlank() // 判断是否为空白
trim() // 去除首尾空格
toUpperCase() // 转换为大写
toLowerCase() // 转换为小写
compareTo(str) // 比较字符串
startsWith(str) // 判断是否以str开头
endsWith(str) // 判断是否以str结尾
```

### 数组

 Java 中数组的定义方式类似于`int[] array`，中括号也可以放在后面（但是不推荐），然后使用`new int[size]`来声明大小。数组是引用类型，长度不可变，可以使用`length`来获取长度，但这个`length`是数组的属性，而不是方法，数组在长度确定后会被设为默认值，也可以在定义时赋予若干值。Java中的`[]`会进行越界检查，如果越界会抛出`ArrayIndexOutOfBoundsException`异常。

### 分支与循环

这个真没有什么不同，注意一下`switch`中的条件不能是`boolean`类型。

Java 中有`for-each`的遍历，格式为：

```java
for (ElementType element : collectionOrArray) {
    // 循环体代码
}
```

Java的标准库已经内置了排序功能，我们只需要调用JDK提供的`Arrays.sort()`就可以排序。

### Package

package 可以方便管理和组织java文件的目录结构，防止不同文件之间的命名冲突

* 作为Java代码源文件的第一条语句，如果缺省则指定为无名包
* 编译器在编译源文件阶段不检查目录结

## 集合类

Java标准库自带的java.util包提供了集合类：Collection，它是除Map外所有其他集合类的根接口。

### List

* 在末尾添加一个元素：`add`
* 在指定索引添加一个元素：`add(int index, Type val)`
* 删除指定索引的元素：`remove(int index)`
* 删除某个元素：`remove(Object val)`
* 获取指定索引的元素：`get(int index)`
* 获取大小（包含元素的个数）：`size()`
* 判断是否包含某个元素：`contains(Object val)`
* 判断是否为空：`isEmpty()`
* 清空：`clear()`

创建`List`

```java
List<Integer> list = List.of(1, 2, 5);
```

Java 中也是有迭代器的
```java
for(var it=list.iterator(); it.hasNext(); ) {
    System.out.println(it.next());
}
```

### HashMap

HashMap用于存储键值对，它主要提供以下几个方法：

* 将键值对添加进HashMap：`put(Type key, Type value)`
* 将键值对从HashMap删除：`remove(Type key)`
* 获取键对应的值：`get(Type key)`
* 判断是否包含某个键：`containsKey(Type key)`
* 判断是否为空：`isEmpty()`
* 清空：`clear()`

遍历可以是遍历键，也可以是遍历值，还可以是遍历键值对。

```java
var map = new HashMap<Integer, String>();
map.put(1, "a");
map.put(2, "b");
map.put(3, "c");

for(var key : map.keySet()) {
    System.out.println(key);
}
for(var value : map.values()) {
    System.out.println(value);
}
for(var entry : map.entrySet()) {
    System.out.println(entry.getKey() + " " + entry.getValue());
}
```

### HashSet

HashSet用于存储不重复的元素集合，它主要提供以下几个方法：

* 将元素添加进Set：`add(Type value)`
* 将元素从Set删除：`remove(Type value)`
* 判断是否包含元素：`contains(Type value)`
* 判断是否为空：`isEmpty()`
* 清空：`clear()`

HashSet 其实是封装了 HashMap，莫名感觉和`GO`殊途同归。

## 异常

Java 中的异常处理和 C++ 差不多，使用`try-catch`来捕获异常，使用`throw`来抛出异常，使用`finally`来执行一些必须执行的代码。

```java
try {
    // 可能会抛出异常的代码
} catch (Exception e) {
    // 捕获异常的代码
} finally {
    // 一定会执行的代码
}
```

## OOP

