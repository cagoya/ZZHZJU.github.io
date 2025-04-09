# 从C++快速入门Java
!!!abstract 内容简介
    本章内容建立在掌握C++的基础上，为从C++到Java的快速入门，只包含Java和C++相像的部分，Java的特性在下一节

## 基础
首先回答一个问题，**为什么Java的main要写在类里面** 这个是第一次看到Java程序会觉得很奇怪的写法，这主要是因为Java中一切皆对象，不允许将方法或者变量暴露在类外。

Java语言的语法和C/C++很接近，所以最基础的基本看一下就会了，这里只列举一些不太一样的东西：
* Java源文件(.java)是先编译成字节码(.class文件)，再由Java虚拟机（JVM）解释执行，此外，JVM的即时编译器（JIT）会在运行时将热点代码（频繁执行的代码）编译为机器码，以提高性能。所以Java比纯解释的代码比如Python要快，但是一般又比纯编译的语言比如C++要慢。
* 主函数：Java里面是写成`public static void main(String[] args)`，这个函数签名是固定的，类似于C的`int main()`，它也是Java程序的入口程序
* 输入输出
  * 输出：`System.out.println`和`System.out.printf`
  * 输入：需要用到`Scanner`类型，要先导入`java.util.Scanner`模块，比如：
```js
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        String name=scanner.nextLine(); //读取一行输入
        int age=scanner.nextInt(); //读取一行输入并获取整数
        //如果没有下一行代码，可能会警告：Resource leak: 'scanner' is never closed
        scanner.close();
        System.out.printf("%s的年龄是%d",name,age);
    }
}
```
* 布尔类型是`boolean`，不能对`boolean`进行类型转换
* 数组的写法略有不同（其实写成C++那样`int arr[5];`也可以过编译，但是不推荐，像下面那样写更符合Java风格：
  * 定义：要用`new`创建，`int[] arr=new int[5]`
  * 遍历：Java也有那个`for each`形式的语法`for(int item:arr)`，但注意Java不提供C++里面那种`auto`自动推导类型，所以要写明类型
  * 排序，`java.util.Arrays`中提供了`Arrays.sort()`
  * 输出，Java直接输出数组会输出哈希码，需要先用`Arrays.toString()`转化成字符串

``` Java
import java.util.Scanner;
import java.util.Arrays;

public class Main{
    public static void main(String[] args){
        int [] arr=new int[10];
        Scanner scanner=new Scanner(System.in);
        for(int i=0;i<arr.length;i++){
            arr[i]=scanner.nextInt();
        }
        scanner.close();
        System.out.print("输出是一个哈希码：");
        System.out.println(arr);
        for(int item:arr){
            System.out.printf("%d ",item);
        }
        System.out.print("\n");
        Arrays.sort(arr);
        //注意是用Array提供的toString而不是写成arr.toString()
        System.out.println(Arrays.toString(arr));
    }
}
//输入1 2 3 4 5 6 7 8 9 10
/*输出
输出是一个哈希码：[I@6ea12c19
1 2 3 4 5 6 7 8 9 10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
*/
```

* 常量使用`final`,`final`同时也可以用于表示类不可被继承
* Java有**垃圾回收机制**，所以根本不需要手动管理内存，自然也就没有`delete`之类的东西
* Java多了一个文档注释`/** */`，这种注释可以被工具提取并生成API文档
* Java也没有指针，提供了引用，除了基本类型的变量名应该都是引用，在传参时也都是引用传递
* 类型转换
  * 低转高是自动的
  * 高转低必须强制类型转换


## 面向对象
### 封装
这部分也是和C++高度相似，Java同样也是有`private`和`public`以及`protected`修饰符，有`this`变量指向当前对象，构造函数与类同名且没有返回值（但是Java要写`public`，否则无法从外部创建对象），通过`new`创建新的对象。

但是`private`的构造函数是真实存在的，因为这种对象是留给`JVM`创建，所谓的私有只是针对编译环节而言。

### 继承
Java提供了`extends`关键字来实现继承，所以没有C++里面的那种私有继承，所有继承一律都是`public`的。Java可以通过`super`调用父类方法（比如调用父类的构造函数），可以用`final`禁止继承。**Java不支持多继承**

Java有一个万物起源的类，也就是`object`，Java中一切类(除了`object`本身)都是继承自`object`，如果定义一个类但是不写是从哪继承就会默认从`object`
继承。

和C++一样，`upcasting`永远是安全的，`downcasting`大概率会失败，Java提供`instanceof`来检验一个变量是否是指定类的实例，但是注意衍生类的确是基类的实例。

### 多态
Java支持函数重载，但**不支持运算符重载**，Java的Override提供了`@Override`进行覆写检查

Java所有方法都相当于C++里面的虚函数，支持**全面的动态绑定**
```java
//基类
class Animal{
    public void makeSound(){
        System.out.println("Animal is making a sound");
    }
}

//派生类1
class Dog extends Animal{
    @Override
    public void makeSound(){
        System.out.println("Dog is barking");
    }
}

//派生类2
class Cat extends Animal{
    @Override
    public void makeSound(){
        System.out.println("Cat is meowing");
    }
}

public class Main{
    public static void main(String[] args){
        //Upcasting
        Animal myAnimal=new Animal();
        Animal myDog=new Dog();
        Animal myCat=new Cat();

        myAnimal.makeSound();
        myDog.makeSound();
        myCat.makeSound();
    }
}
//结果：
/*
Animal is making a sound
Dog is barking
Cat is meowing
*/
```

### 接口
Java中抽象类用`abstract`修饰，抽象类是不能被实例化的类，通常用于作为其他类的基类。它可以包含抽象方法（没有实现的方法）和具体方法（有实现的方法）。
```java
abstract class Animal{
    //抽象方法
    public abstract void makeSound();
    //具体方法
    public void sleep(){
        System.out.println("Sleeping...");
    }
}

class Dog extends Animal{
    @Override
    public void makeSound(){
        System.out.println("woof");
    }
}
```
Java有接口类`interface`，接口是一种完全抽象的类，它只能包含抽象方法（在Java 8之前）和常量（public static final变量）。从Java 8开始，接口可以包含默认方法（default methods）和静态方法（static methods）。
```java
interface Animal {
    void makeSound();

    default void sleep(){
        System.out.println("Sleeping...");
    }

    static void breathe(){
        System.out.println("Breathing...");
    }
}
```

## 异常

这个也是和C++几乎是一样的，有`try...catch`模块和`throw`关键字，这里给一个自定义异常的例子
```java
// 自定义异常类
class MyCustomException extends Exception{
    public MyCustomException(String message){
      super(message);
    }
  }
  
  public class Main{
    public static void main(String[] args){
      try{
        //调用一个抛出异常的方法
        checkAge(16);
      }catch(MyCustomException e){
        System.out.println("捕获到异常："+e.getMessage());
      }
    }
  
    public static void checkAge(int age) throws MyCustomException{
      if(age<18){
        throw new MyCustomException("年龄不能小于18岁");
      }
      else{
        System.out.println("年龄合法");
      }
    }
  }
// 输出：捕获到异常：年龄不能小于18岁
```
## 数据结构

Java 提供了丰富的数据结构，类似于 C++ 的标准模板库（STL）。以下是 Java 中常见的数据结构及其与 C++ 的类比关系：

- **Arrays**：类似于 C++ 的静态数组。
- **ArrayList**：类似于 C++ 的 `vector`，即动态数组。
- **LinkedList**：双向链表。
- **Set**
  - **HashSet**：无序集合，底层实现为哈希表。
  - **TreeSet**：有序集合，底层实现为红黑树，不允许重复元素。
- **Map**
  - **HashMap**：无序映射，底层实现为哈希表。
  - **TreeMap**：有序映射，底层实现为红黑树。
- **Stack**：类似于 C++ 的栈。
- **Queue**：类似于 C++ 的队列。Java 还提供了优先队列（`PriorityQueue`）和双端队列（`Deque`）。
- **TreeNode**：Java 提供了树的节点类型，可能是由于 Java 没有指针，直接提供了树的节点类型。
- **枚举**：Java 的枚举是类

Java 同样实现了常见的算法和迭代器

```java
// 使用泛型的 HashMap 示例
HashMap<Integer, String> map = new HashMap<>();
map.put(1, "One");
map.put(2, "Two");
```



## 泛型

Java 的泛型（Generics）类似于 C++ 的模板（Templates），允许开发者编写通用的、类型安全的代码。通过泛型，可以在编译时进行类型检查，减少运行时错误。

### 泛型类

```java
//泛型类
public class Box<T> {
    private T item;

    public void setItem(T item) {
        this.item = item;
    }

    public T getItem() {
        return item;
    }
}

```

### 泛型函数

```java
//泛型函数
public <T> void printArray(T[] array) {
    for (T element : array) {
        System.out.println(element);
    }
}
```

### 通配符与边界

####  通配符

* `<?>`：表示任意类型，就类似于C++的auto
* `<? extend T>`：表示`T`或者`T`的子类型
* `<? super >`：表示`T`或者`T`的父类型

#### 边界

可以限制参数的范围

```java
public <T extends Comparable<T>> T max(T a, T b) {
    return a.compareTo(b) > 0 ? a : b;
}
```