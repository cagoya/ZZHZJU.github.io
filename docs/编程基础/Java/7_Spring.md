# Spring

!!!abstract Why Spring?
    Spring makes programming Java quicker, easier, and safer for everybody. Spring’s focus on speed, simplicity, and productivity has made it the world's most popular Java framework.—— Spring 官方文档

## 简介
### Spring的地位
[Spring](https://spring.io/) 是全世界最流行的 Java 框架（没有之一）,Spring发展到今天已经不再是简单的框架，而是一个庞大的生态圈，现代的Java开发基本就是依赖于Spring的。

### 依赖注入
Spring 框架的核心功能是：
* 负责创建、管理所有的Java对象，这些Java对象被称作bean
* 管理容器中bean之间的依赖关系，这里会用到依赖注入

控制反转（IoC）和依赖注入（DI）本质上是一个事物的两面，IoC是设计思想，DI是实现方式。在传统模式下，如果一个Java对象要调用另一个依赖的对象，则必须得由调用程序主动创建被调用对象，或者去被调用对象的管理程序中获取，这样必然会导致调用对象与依赖对象之间的耦合。

使用Spring框架之后，调用程序获取被依赖对象由**主动**获取变成了**被动**接受，依赖对象是被注入到调用程序的，所以叫做“依赖注入”，与此同时，对于依赖对象的控制权由调用程序转移到了容器，所以也叫“控制反转”。

## 分层解耦
### 三层架构

![alt text](images\three_layer.png)

* 控制层：接收前端发送的请求，对请求进行处理，并响应数据
* 业务逻辑层：处理具体业务逻辑
* 数据访问层：也叫持久层，负责数据访问操作，包括数据的增删改查

### Spring解耦
聚合指的是软件各个模块内部的功能联系，耦合衡量各个层的依赖、关联程度，软件设计需要高聚合，低耦合。Spring解耦的手段是提供一个容器作为中间连接，对象交由容器管理，从而避免调用程序主动去管理依赖对象。

## IoC & DI
### 实现
把Service和Dao层的实现类交给IoC Container管理，使用`@component`注解

## AOP