# Java 进阶
!!!abstract
    本节是Java重要特性的合集，包括反射、注解、包等知识

## 包
相当于C++的命名空间，把功能相似或相关的类或接口组织在一个包中，方便类的查找和使用，不同包中的类名字可以相同。比如：
```java
//package必须写在最前面，除了注释
package net.java.util;
public class Something{
  ...
}
```
那么它的路径就应该是`net/java/Something.java`

但是源文件是有声明规则的，当在一个源文件中定义多个类，并且还有`import`和`package`语句时，需要特别注意这些规则：

* 一个源文件只能有一个`public`类，可以有多个非`public`类，**源文件名称应与`public`类保持一致**
* 如果一个类定义在某个包中，`package`语句应该放在第一行，`import`语句紧随其后
* `import`和`package`都是全局有效的，在同一个源文件中，不能给不同类不同的包声明

## 反射
这是一个新概念，是一个强大的特性，提供了动态操作类的能力，允许程序在运行时查询、访问和修改类、接口、字段和方法的信息。通常有以下**工作流程**：
* 获取Class对象：首先获取目标类的Class对象
* 获取成员信息：通过Class对象，可以获取类的字段、方法、构造函数等信息
* 操作成员：通过反射API可以读取和修改字段的值、调用方法以及创建对象

Java提供了以下API：

* `java.lang.Class`:表示类的对象
* `java.lang.reflect.Fielf`:表示类的对象
* `java.lang.reflect.Method`:表示类的方法
* `java.lang.reflect.Constructor`:表示类的构造函数

但是反射也有缺点：

* **破坏了封装性**：你都能从外面获取类内部的信息了，可见封装被破坏了
* **性能开销大**：反射的性能比直接写要差很多，因为是动态执行的，不好优化

![img](https://www.runoob.com/wp-content/uploads/2024/08/javalang.png)

`class`是由`JVM`在运行过程中**动态加载的**，`JVM`在读到一种`class`类型时，将其加载进内存，每加载一个`class`，`JVM`就为它创建一个`Class`实例，并关联起来，一个`Class`实例包含了`class`的全部信息，所以如果我们获取了一个`Class`实例，那么`class`的全部信息也就已知了，这个过程就叫做反射。

**Java**由于版本更新，这部分很多方法都已经弃用或者改进了，网上很多教程都过时了，建议真的得去编译器试试。

#### 获取`Class`

有三种方法获取`Class`：
* 直接访问 类 的 class 属性
* 通过实例变量获取
* 通过完整类名获取

```java
// <?> 表示任意泛型
Class<?> cls1 = String.class;
String s = "Hello";
Class<?> cls2 = s.getClass();
Class<?> cls3 = Class.forName("java.lang.String");
```

#### 创建新对象
获取类的构造函数然后调用，通过反射拿到的函数可以和正常的函数一样地使用
```java
Class<?> cls = String.class;
Constructor<?> Constructor = cls.getConstructor(cls);
String s2 = (String) Constructor.newInstance("Hello, World!");
System.out.println("s2: " + s2); // 输出: s3: Hello, World!
```

#### 获取类的信息
这个就是调用相应的函数就可以知道相应信息，类名，修饰符，父类，接口都可以获取
```java
Class<?> clazz = String.class;
// 获取类名
System.out.println("类名: " + clazz.getName()); // 输出: java.lang.String
```

#### 获取字段
java里面一般把变量叫做字段，这个不仅可以获得public字段，还可以获取private字段
```java
class Person {
    private String name;
    public int age;
}
Class<?> clazz = Person.class;

// 获取所有字段（包括 private）
Field[] allFields = clazz.getDeclaredFields();
for (Field field : allFields) {
    System.out.println("字段: " + field.getName()); // 输出: name, age
}
```

#### 获取方法
反射可以获取方法
```java
class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}
Class<?> clazz = Calculator.class;
// 获取所有 public 方法
Method[] methods = clazz.getMethods();
for (Method method : methods) {
    System.out.println("方法: " + method.getName());
}
// 调用 public 方法
Calculator calculator = new Calculator();
Method addMethod = clazz.getMethod("add", int.class, int.class);
int result = (int) addMethod.invoke(calculator, 10, 20);
System.out.println("add 结果: " + result); // 输出: 30
```

## 注解
注解(Annotation)是Java的一种注释机制，Java 语言中的类、方法、变量、参数和包等都可以被标注。`@override`在java中其实就是一种注解
### 内置注解
Java 定义了一套注解，共有 7 个，3 个在 java.lang 中，剩下 4 个在 java.lang.annotation 中。

作用在代码的注解是：
* `@Override`: 表示方法重写了父类中的方法。如果方法没有正确重写，编译器会报错。
* `@Deprecated`：标记类、方法、字段已经过时，不推荐使用。编译器会发出警告
* `@Surpresswarning`：抑制编译器警告

作用在其它注解的注解，或者说元注解是：
* `@Rentention`：表示这个注解怎么保存，是只在源代码中，还是编入class文件中，或者是在运行时可以通过反射访问
* `@Documented`：标记这些注解是否在用户文档中
* `@Target`：标记这个注解的对象是哪种java成员
* `@Inherit`：标记注解是继承自哪个注解

### 自定义注解
可以通过`@interface`关键字自定义注解
```java
import java.lang.annotation.*;

@Target(ElementType.METHOD) // 注解用于方法
@Retention(RetentionPolicy.RUNTIME) // 注解在运行时保留
public @interface MyAnnotation {
    String value() default "default value"; // 注解属性
    int count() default 0; // 另一个注解属性
}
```