# Maven
## 简介
### 功能
Maven是当今Java开发中主流的依赖管理工具，Maven,IDEA 安装时自带了默认的Maven，也可以自己配置，**Maven可以用于管理jar包、提供统一的项目结构以及自动化项目构建。**



自己安装并导入环境变量后，在`cmd`输入`mvn -version`可以得到类似的结果，这里显示`jdk`版本是`22.0.1`,`maven`版本是`3.9.9`

![alt text](images\maven.png)

Meaven 由于是从国外下载，所以最好也是用阿里云镜像，修改配置文件即可

### 目录
使用Maven管理的java项目，它的目录结果大概是
```
项目根目录/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/            # 主代码目录
│   │   └── webapp/          # Web 应用的资源目录（如果是 Web 项目）
│   └── test/
│       ├── java/            # 测试代码目录
│       └── resources/       # 测试资源文件
└── target/                  # 构建输出目录（编译后的类文件、打包的 JAR/WAR 等） 
```

* **pom.xml是 Maven 项目的核心配置文件**，定义了项目的依赖、插件、构建配置等信息
* src/main/java，存放项目的主代码（Java 源文件），按照包结构组织
* src/main/webapp，如果是一个 Web 项目（如 Servlet、Spring MVC 等），这个目录会存放 Web 相关的资源，如 WEB-INF/web.xml、JSP 文件、静态资源（HTML、CSS、JS 等）
* target，这是 Maven 构建过程中生成的输出目录，包含编译后的类文件、打包的 JAR/WAR 文件、测试报告等。

Maven 通过各种插件来完成项目构建

![alt text](images\pom.png)

### jar
JAR（Java Archive）是一种用于打包Java类文件、资源文件和元数据的压缩文件格式，通常以.jar为扩展名。它基于ZIP格式，能够将多个文件合并为一个文件，便于分发和部署Java应用程序。

正常情况下需要导入jar包时要手动去官网下载然后复制到当前工程目录，但是这样未免太麻烦，而且实际开发时会遇到海量的jar包，所以需要maven这种包管理器，有了它之后就可以自动下载jar并导入。

## 项目依赖
### pom.xml
当执行一个任务或者目标时，Maven 会查找当前目录下的 POM，从其中读取所需要的配置信息，然后执行目标,Maven 会自动从中央仓库下载依赖并存储到本地仓库。在创建 POM 之前，首先确定工程组（groupId），及其名称（artifactId）和版本，在仓库中这些属性是工程的唯一标识。这里以获取mysql的驱动jar为例
```xml
<!--当前项目信息，这里略去 -->

<dependencies>
    <dependency>
        <!--工程组的标识,它在一个组织或者项目中通常是唯一的,公司或域名倒序+项目名-->
        <groupId>mysql</groupId>
        <!--工程的名称,模块名-->
        <artifactId>mysql-connector-java</artifactId>
        <!--工程的版本号-->
        <version>9.0.1</version>
        <!--scope标签代表指定依赖范围-->
        <scope>runtime</scope>
    </dependency>
    ...
</dependencies>
```
这个依赖如果是还未下载到本地的包话需要去官网查询相应的`dependency`，导入成功的话，可以在外部库栏查看到相应库。

### 依赖传递
一个库可能要依赖于其他库，这是很正常的，比如下面那个`mysql`库，

![alt text](images\dependency.png)

比如A依赖B，B依赖C，默认情况下A是依赖C的，但是我们可以排除依赖
```xml
<exclusion>
    <groupId>xxx</groupId>
    <artifactId>xxx</artifactId>
    <!--排除依赖不需要写版本-->
</exclusion>
```

### 依赖范围
默认状态下导入的jar是在当前工程有效，但是我们可以指定jar包的作用范围

| scope值    | 主程序    | 测试程序   | 打包（运行） | 范例    |
|---|---|---|---|---|
| compile（默认）    | Y    | Y    | Y    | log4j    |
| test    | -    | Y    | -    | junit    |
| provided    | Y    | Y    | -    | servlet-api    |
| runtime    | -    | Y    | Y    | jdbc驱动    |

可以用`<scope></scope>`注明依赖范围

### 生命周期
Maven有三套生命周期，阶段很多，但是我们主要注意下面这五个就好：
* clean:clean
* default:complie,test,package,install
* site
它们的作用如下：
1. **clean**: 移除上一次构建生成的文件
2. **compile**: 编译项目源代码
3. **test**: 使用合适的单元测试框架运行测试（如 JUnit）
4. **package**: 将编译后的文件打包，如：jar、war 等
5. **install**: 安装项目到本地仓库

在同一个生命周期中运行后面的声明周期阶段时，也会运行前面的