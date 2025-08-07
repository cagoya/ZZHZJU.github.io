# Java

> 这里是站在已经掌握了 C++ 的基础上来学习 Java 的，所以一些完全相同的东西就不再赘述了。

## 简介

Java 最早是针对小型家电设备的嵌入式应用开发而设计的语言，最开始反响平平，但是后来互联网兴起后，Java成为了互联网开发的主流语言。Java 介于解释型和编译型语言之间，先将代码编译成一种“字节码”，再由JVM解释执行。

随着Java的发展，Java又分出了三个不同版本的规范：

* Java SE：Standard Edition
* Java EE：Enterprise Edition
* Java ME：Micro Edition

它们之间的包含关系是$\text{ME} \subset \text{EE} \subset \text{SE}$，但是Java ME从未真正流行过，Java EE 也已经停止更新。

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

Java 中所有方法和变量都必须定义在类中，`JVM`默认`main`函数是程序的入口，并且这个函数应该是`static`的，如果没有运行时会报错。

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

1. Java只定义了带符号的整型
2. Java对布尔类型的存储并没有做规定，通常JVM内部会把`boolean`表示为4字节整数
3. Java的`char`类型除了可表示标准的ASCII外，还可以表示一个Unicode字符，无论中英文都是占两个字节

除了上述基本类型的变量，剩下的都是**引用类型**，在Java中，引用类型的变量非常类似于C/C++的指针，引用类型指向一个对象，所有引用类型的默认值都是`null`。对于基本类型，Java提供了对应的包装类型，比如`int`对应的包装类型是`Integer`，`Integer`就是一个引用类型，这个主要是为了方便引用传参。

常量使用`final`关键字定义，也就是`C++`里面的`const`，除此之外`final`还可以用于限制方法和类，限制方法后，该方法不能被重写，限制类后，该类不能被继承。此外，Java 支持使用`var`来进行自动类型推断，用法同C++的`auto`。

Java中的类型转换还是和C++差不多，对于`short + int`这种会自动向上提升为`int`，即隐式类型转换，显式类型转换还是类似于`(int) a`。

### 字符串

`String`是引用类型，Java中的`String`也是支持`+`的（这个只能说是特殊考虑，`Java`其实是不支持运算符重载的），对于非字符串类型，`Java`会自动尝试类型转换。

```java
int age = 15;
String name = "Tom";
String res = name + ":" + age; // "Tom:15"
```

对于格式化字符串，Java支持使用`String.format()`来格式化字符串。
```java
String res = String.format("%s:%d", name, age); // "Tom:15"
```

Java 支持多行字符串，和Python一样是三引号`"""`，此外Java中的字符串同样是不可变的。最后，这里给出一些常用的方法，基本是如今高级语言都会有的，对于单个字符：

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
equals(str) // 判断是否相等
isBlank() // 判断是否为空白
trim() // 去除首尾空格
toUpperCase() // 转换为大写
toLowerCase() // 转换为小写
compareTo(str) // 比较字符串
startsWith(str) // 判断是否以str开头
endsWith(str) // 判断是否以str结尾
```

### 数组

Java 中的数组是引用类型，定义方式如下，中括号也可以放在后面（但是不推荐）

```java
int[] arr1 = new int[5];
var arr2 = new int[3]{1, 2, 3};
```

可以使用`length`来获取长度，但这个`length`是数组的属性，而不是方法。

```java
int length1 = arr1.length;
```

数组中的元素如果未进行赋值会被自动设为默认值，Java中的`[]`会进行越界检查，如果越界会抛出`ArrayIndexOutOfBoundsException`异常。

Java的标准库已经内置了排序功能，我们只需要调用JDK提供的`Arrays.sort()`就可以排序。

```java
Arrays.sort(arr);
```

如果需要自定义排序规则，可以传入一个`Comparator`。

```java
Arrays.sort(arr, (a, b) -> a > b ? 1 : -1);
```

### lambda 表达式

上面的`Arrays.sort(arr, (a, b) -> a > b ? 1 : -1);`就是使用了 lambda 表达式，lambda 表达式是 Java 8 引入的，它提供了一种简洁的方式来表示匿名函数，本质是函数式接口的一个匿名实现。函数式接口是指只包含一个抽象方法的接口，Java 8 在 `java.util.function` 包中预定义了许多常用的函数式接口，例如：

* `Consumer<T>`：接收一个参数，没有返回值。
* `Predicate<T>`：接收一个参数，返回一个 boolean 类型的值。
* `Function<T, R>`：接收一个 T 类型的参数，返回一个 R 类型的值。
* `Supplier<T>`：不接收参数，返回一个 T 类型的值。

Lambda 表达式的基本语法如下：

```java
(参数列表) -> { 表达式或代码块 }
```

Lambda 表达式还有一种更简洁的形式，叫做方法引用（Method Reference），类似于函数指针。当 Lambda 表达式只是简单地调用一个已存在的方法时，可以使用方法引用来代替。

```java
// Lambda 表达式
List<String> names = Arrays.asList("peter", "anna", "mike", "xenia");
names.forEach(name -> System.out.println(name));

// 方法引用
names.forEach(System.out::println);
```

### 分支与循环

这个真和C++没有什么不同，都是`if-else`，`switch`，`while`，`do-while`，`for`和`for-each`，并且有`break`和`continue`。

Java 中的`for-each`的遍历，格式一般为：

```java
for (ElementType element : collectionOrArray) {
    // 循环体代码
}
```

比如对于数组

```java
int[] arr = {1, 2, 3, 4, 5};
for (int i : arr) {
    System.out.println(i);
}
```

### 输入输出

#### 流

* 字节流是所有 I/O 的基础，其抽象基类分别是`InputStream`和`OutputStream`。
* 字符流是字节流的包装，其抽象基类分别是 Reader 和 Writer。它们通常用于处理文本文件。
  * FileReader：从文件中读取字符。
  * FileWriter：向文件中写入字符。

```java
try (
    FileReader fr = new FileReader("source.txt");
    FileWriter fw = new FileWriter("destination.txt")
) {
    int charRead;
    // 每次读取一个字符，直到文件末尾
    while ((charRead = fr.read()) != -1) {
        fw.write(charRead);
    }
    System.out.println("文件复制成功！");
} catch (IOException e) {
    e.printStackTrace();
}
```

* 缓冲流是对基本 I/O 流的装饰，它们在内存中设置一个缓冲区，批量读写数据，从而大大提高效率。

#### 标准输入输出

Java 的标准输入输出（键盘输入和屏幕输出）也通过流来实现：

* 标准输入流：`System.in`（类型为`InputStream`）。
* 标准输出流：`System.out`（类型为`PrintStream`）。
* 标准错误流：`System.err`（类型为`PrintStream`）。

在实际开发中，我们通常会使用 Scanner 类或 BufferedReader 来方便地处理键盘输入。

使用 Scanner 读取键盘输入：

```java
Scanner scanner = new Scanner(System.in);

System.out.print("请输入你的名字：");
String name = scanner.nextLine();

System.out.print("请输入你的年龄：");
int age = scanner.nextInt();

System.out.println("你好，" + name + "！你今年 " + age + " 岁。");

scanner.close();
```

### Package

package 可以方便管理和组织java文件的目录结构，防止不同文件之间的命名冲突，类似于命名空间，package 作为Java代码源文件的第一条语句，如果缺省则指定为无名包。package是一个多层的树形结构，比如JDK的Arrays类存放在包`java.util`下面，因此，完整类名是`java.util.Arrays`，编译后的`.class`文件和源文件的目录结构保持一致，在JVM中运行时只看完整的类名。

使用`import`语句可以导入其他包中的类，`import`语句可以放在文件的任何位置，但是通常放在文件的开头。

```java
// 导入java.util包中的Arrays类
import java.util.Arrays;
```

如果需要导入包中的所有类，可以使用`*`，但是不推荐。

```java
import java.util.*;
```

## 集合类

Java标准库自带的java.util包提供了集合类：`Collection`，它是除`Map`外所有其他集合类的根接口，这里主要讨论最常用的三个具体的集合类，除此以外，基础数据结构中的`Stack`，`Queue`，`PriorityQueue`也都是有的。

### ArrayList

List 代表一个可变长的数组，即C++中的`vector`，本身是一个接口，Java中提供了`ArrayList`和`LinkedList`两种实现，前者基于数组实现，后者基于链表实现，这个接口包含了以下方法：

* 在末尾添加一个元素：`add`
* 在指定索引添加一个元素：`add(int index, Type val)`
* 删除某个元素：`remove(Type val)`
* 删除指定索引的元素：`remove(int index)`
* 获取指定索引的元素：`get(int index)`
* 获取大小（包含元素的个数）：`size()`
* 判断是否包含某个元素：`contains(Type val)`
* 判断是否为空：`isEmpty()`
* 清空：`clear()`

创建`List`，这里使用`ArrayList`

```java
var list = new ArrayList<Integer>();
```

Java 中也是有迭代器的，迭代器的遍历效率往往最高

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

HashSet 相当于封装了 HashMap，值全为`null`，莫名感觉和`GO`殊途同归。

## 异常

Java 中的异常处理和 C++ 差不多，使用经典的`try-catch`来捕获异常，使用`throw`来抛出异常，使用`finally`来执行一些必须执行的代码。

```java
try {
    // 可能会抛出异常的代码
} catch (Exception e) {
    // 捕获异常的代码
} finally {
    // 一定会执行的代码
}
```

Java 中的异常类都是继承自`Exception`，自定义异常时一般是选择一个异常作为根异常，然后在此基础上继承，通常会选择`RuntimeException`作为根异常。

```java
public class MyException extends RuntimeException {
    public MyException(String message) {
        super(message);
    }
}
```

Java 的断言也是异常，使用`assert`关键字，断言失败会抛出`AssertionError`异常。

```java
int a,b;
System.in.readInteger(a);
System.in.readInteger(b);
assert b != 0 : "b cannot be 0";
System.out.println(a/b);
```

JVM默认关闭断言指令，即遇到assert语句就自动忽略了，不执行。要执行assert语句，必须给Java虚拟机传递`-enableassertions`（可简写为`-ea`）参数启用断言。

## 面向对象

### 方法

Java 中访问修饰符有`public`，`private`和`protected`以及`static`，然后参数只支持按位置传递，有变长参数，也有`this`变量指向当前对象，方法重载也是支持的。

```java
public class Test {
    // 经典的重载
    public void test(int a, int b) {
        System.out.println(a + b);
    }

    public void test(double a, double b) {
        System.out.println(a + b);
    }

    // 可变长参数
    public void test(String... args) {
        for (String arg : args) {
            System.out.println(arg);
        }
    }
}
```

构造函数依旧是如果没有编译器会给一个默认的，并且可以给字段默认值，如果没有显式写出，那么默认值就是对应类型的默认值，比如`int`的默认值是`0`。

```java
public class Test {
    int a = 1;
    int b = 2;
    public Test() {
        
    }

    public Test(int a, int b) {
        this.a = a;
        this.b = b;
    }
}
```

### 继承

Java 所有类最终都继承自`Object`，Java中只能单继承，继承使用`extends`关键字，Java 中有`super`关键字表示父类，子类引用父类的字段时，可以用`super.fieldName`，但是没有必要，`super`主要用于调用父类的构造函数`super()`。

还是一样，向上转型是安全的，向下转型则不一定，Java 中有`instanceof`关键字来判断类型。

```java
if (obj instanceof Test) {
    Test test = (Test) obj;
}
```

### 多态

Java 重写父类方法时，需要使用`@Override`注解，重写方法时，参数列表必须和父类方法一致，返回类型必须是父类方法返回类型的子类型，或者`void`。Java 支持全面的动态绑定，也就是不需要声明虚函数。

Java 提供`abstract`关键字来定义抽象类和抽象方法，抽象类不能被实例化，抽象方法没有方法体，只有方法签名。

```java
// 这是一个抽象类，只用于被继承
public abstract class Test {
    // 这是一个抽象方法，没有方法体
    public abstract void test();
}
```

但是对于一个全是抽象方法的类，更推荐写为`Interface`，接口只规约需要实现的方法，不允许有字段，并且默认方法是`public abstract`的，实现接口使用`implements`关键字，Java 中允许实现多个接口。

```java
public interface Test {
    public void test();
}
```

### 泛型

通常来说，泛型类一般用在集合类中，例如`ArrayList<T>`，我们很少需要编写泛型类。

```java
// 泛型类 Box，可以存放任何类型的对象
public class Box<T> {
    private T t;

    public void set(T t) {
        this.t = t;
    }

    public T get() {
        return t;
    }
}
```

在没有泛型之前，对于这种`List`，可能需要创建一个可以存放 Object 的类，然后在取出时进行强制类型转换，这会带来运行时 ClassCastException 的风险。

泛型接口的定义方式与泛型类类似。

```java
public interface MyList<E> {
    void add(E e);
    E get(int index);
}

public class MyArrayList<E> implements MyList<E> {
    // ... 实现接口方法
}
```

泛型方法可以在任何类中定义，无论该类是否是泛型类。类型参数`<T>`放在方法的返回类型之前。

```java
// 泛型方法，可以打印任何类型的数组
public static <T> void printArray(T[] array) {
    for (T element : array) {
        System.out.printf("%s ", element);
    }
    System.out.println();
}
```

有时可能需要处理未知类型的泛型，这时就需要使用通配符`?`。上界通配符：`<? extends T>`表示类型是 T 或 T 的子类。这通常用于读取数据的场景。

```java
public void printList(List<? extends Number> list) {
    for (Number num : list) {
        System.out.println(num);
    }
}
```

下界通配符：`<? super T>`表示类型是 T 或 T 的父类。这通常用于写入数据的场景。

```java
public void addNumbers(List<? super Integer> list) {
    for (int i = 1; i <= 10; i++) {
        list.add(i);
    }
}
```

## 反射

反射指的是在运行期间可以拿到一个对象的全部信息，然后可以动态地访问和修改对象的属性和方法。

