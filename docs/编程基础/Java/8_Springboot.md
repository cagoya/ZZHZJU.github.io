# Springboot
## 简介
[Spring](https://spring.io/) 是全世界最流行的 Java 框架（没有之一，现代的Java开发基本就是依赖于Spring的。

**Sringboot 并不是对 Spring功能上的增强，而是提供了一种快速使用Spring的方式**，学习起来比Spring更加简单，可以快速入门。Springboot有如下优势：
* 自动配置：Spring 会分析项目的依赖关系，自动配置应用程序所需的 Bean 和其他设置。
* 起步依赖：Spring Boot 提供了一系列的“起步依赖”（Starter Dependencies），这些依赖项将常用的库和框架组合在一起，简化了项目的依赖管理。

## 快速入门
在 IDEA 创建Springboot项目是很容易的，只需要选中创建Spring项目(spring web)，然后就会自动从官网下载配置文件，大概是下面这种效果，如果要自己配置就需要自己填写`pom.xml`

`pom.xml`中会存在如下几行，任何`spring`工程都是继承自父工程

![alt text](images\spring.png)

这里以一个`hello world`为例，写一个`hello world`的`controller`类
```java
//请求处理类
@RestController
public class HelloworldController {
    //指定请求路径
    @RequestMapping("/hello")
    public String hello(){
        System.out.println("Hello World!");
        return "Hello World!";
    }
}
```

然后运行 Spring启动程序，可以在`localhost:8080/hello`看到输出，`loacalhost:8080`应该没有内容，而是会有一段报错，这是因为一个web服务器可以挂载多个网页，所以需要约定请求路径，即这里的`/hello`

![alt text](images\hello.png)

## 请求响应
在后端开发中，每开发完一个模块就需要进行测试，但是如果是在浏览器里面访问，由于浏览器地址栏只能发起GET请求，测试POST请求会很麻烦，可能需要编写前端代码，所以我们需要一些额外的工具，这里我们选用`apifox`

<img src=images\apifox.png width=500>

### 原始方式
原始的方式需要用到`HttpServletRequest`对象，并且需要手动进行类型转换

```java
@RestController
public class RequestController {
    @RequestMapping("/simpleParam")
    public String simpleParam(HttpServletRequest request){
        String name = request.getParameter("name");
        String ageStr = request.getParameter("age");
        int age = Integer.parseInt(ageStr);
        System.out.println("name:" + name + ", age:" + age);
        return "Hello " + name + ", " + age;
    }
}
```

### Spring Boot 方式
#### 不同参数接收方式
Springboot方式下可以直接接受转换好类型的参数，相比之下更为简洁。
```java
//暴露的接口
@RestController
public class RequestController {
    //指定返回路径
    @RequestMapping("/simpleParam")
    //从HTTP中接受参数
    public String simpleParam(String name, Integer age) {
        System.out.println("name:" + name + ", age:" + age);
        //返回值
        return "Hello " + name + ", " + age;
    }
}
```

默认情况下，Spring Boot 允许 `POST` 请求的参数以 `application/x-www-form-urlencoded` 形式提交，例如：
```java
@RestController
public class RequestController {
    @PostMapping("/postParam")
    //使用@RequiredParam绑定参数
    public String postParam(@RequestParam("name") String name, @RequestParam("age") Integer age) {
        System.out.println("name:" + name + ", age:" + age);
        return "Hello " + name + ", " + age;
    }
}
```

注意如果 `@RequestParam` 未指定 `required = false`，那么该参数默认是必须的。

此外Springboot还支持以下形式的参数：

* 可以将多个参数封装到对象中，前提是请求参数的键名要与对象的属性名一致。
* 如果参数是 JSON 格式，则需要使用 `@RequestBody` 进行绑定。
* 数组和集合，集合类型需要使用 `@RequestParam` 绑定参数。
* 时间格式化参数，Java中时间表示有多种形式，可以使用 `@DateTimeFormat` 注解来解析不同的时间格式。
* JSON格式参数需要使用 `@RequestBody` 绑定。
* 路径参数在 URL 中的参数可以使用 `{}` 进行占位，并通过`@PathVariable` 绑定。


#### 统一响应结果
因为如果不加限制，前端可以想怎么返回就怎么返回，这对于维护项目是不利的，所以我们约定选用一个`result`对象返回，如
```java
public class Result{
    //响应码 1代表成功，0代表失败
    private Integer code;
    //提示信息
    private String msg;
    //返回数据
    private Object data;
}
```

### 分层解耦
#### 三层架构

![alt text](images\three_layer.png)

* 控制层：接收前端发送的请求，对请求进行处理，并响应数据
* 业务逻辑层：处理具体业务逻辑
* 数据访问层：也叫持久层，负责数据访问操作，包括数据的增删改查

#### 分层解耦
内聚指的是软件各个模块内部的功能联系，耦合衡量各个层的依赖、关联程度，软件设计需要高内聚，低耦合。

提供一个容器作为中间连接，对象交由容器管理

#### IOC
控制反转(Inversion of Control)，对象的管理权由创建程序自身转移至外部（容器），只需要在类上加上`@Component`，使对象变为IOC的bean对象。

在`@Component`之上衍生出了三个针对每个层的注解：
* `@Controlller`
* `@Service`
* `@Repository`

#### DI
依赖注入(Dependency Injection)，容器为应用程序提供运行时所依赖的资源，称之为依赖注入，需要在对象上加`@Autowired`。