# Web 基础
## BS 体系
如今的web几乎都是**B/S架构(Browser/Server)**，它的特点是客户端只需要浏览器，应用数据和逻辑都在服务器，所以只需要维护服务端。在Web应用中，浏览器请求一个URL，服务器就把生成的HTML网页发送给浏览器。

<img src = "images\BS.png" width = 300>

平时访问的网页，比如淘宝、天猫这种都是BS架构，但其实还有另一种架构也比较常见，那就是CS架构，即客户端-服务器架构，比如微信和QQ就是基于这种架构，需要安装单独的客户端，这些客户端会因为操作系统而异。

### Web 分类
Web 可以分为：
* 静态 web是预先创建好的HTML文件，内容固定不变，用户每次访问时看到的内容相同，这部分由html、CSS、JS就可以完成，适用于内容不频繁变化的网站，如个人博客
* 动态 web:提供给所有的人看的数据始终会变化，每个人在不同的时间，不同的地点看到不同的信息，**实际当中大部分网站都是动态的**

### java EE
即Java 企业版，包含13项技术规范，其中后端开发会涉及到的有JDBC，JSP，Servlet，XML，但其实这里面大部分都较为过时，现在流行的是基于这些的更高级的框架

## HTTP
HTTP(超文本传输协议)规定了浏览器和服务器之间数据传输的规则。HTTP基于TCP协议，面相连接安全，一次请求对应一次响应，此外，HTTP是无状态的，对于事务没有记忆能力，这个会影响到后面HTTP的鉴权。

![alt text](images\http.png)

HTTP常见以下四种请求：
* GET：请求服务器发送指定资源，通常用于获取数据，不应修改服务器上的数据。请求数据会以?形式拼接在请求头(header)中，不安全，没有请求实体部分
* POST：向服务器提交数据，通常用于表单提交或创建资源。请求数据在请求实体(body)中进行发送，在URL中看不到具体请求类型
* PUT：更新或创建资源（如果资源不存在）。
* DELETE：请求服务器删除指定资源。

## TomeCat
### web服务器
web服务器是一个软件程序，对HTTP协议的操作进行封装，使得程序员不必直接对HTTP进行操作。

### 简介
Apache Tomcat 是Java Servlet、JavaServer Pages （JSP）、Java表达式语言和Java的WebSocket技术的一个开源实现，直接在TomCat就可以下载。

* bin - 可执行文件
* conf - 配置文件
* lib Tomcat依赖的jar包
* logs - 日志文件
* temp - 临时文件
* webapps 应用发布目录
* work - 工作目录

配置好环境变量在`cmd`输入`startup`就可以运行TomeCat，TomCat默认是utf-8编码，需要改成GBK，否则中文会乱码。TomCat默认使用的是8080端口，这个也是可以修改的，在`conf\server.xml`。启动后通过浏览器访问可以看到如下界面：

<img src = "images\TomCat.png" width=500>

### 基本使用
将项目放到`webapp`目录下就算完成部署，因为框架会内置TomCat，所以我们并不会直接使用这个原生的TomCat

## Servlet与JSP
Java EE 提供 Servlet 接口，基于请求响应模型处理HTTP，下面是一个简单的Servlet实例。实际当中，我们如今并不会直接使用`Servlet`，而是会选择使用Spring框架。
```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

//映射页面
@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        //将HTTP输出到页面
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<h1>Hello, World!</h1>");
        out.println("</body></html>");
    }
}
```
可以看到以上程序输出虽然只有一句话，但是已经用了三行输出，为了输出更大段的`html`，比如一个完整的页面，我们有没有更好的办法？

<del>有的，兄弟，有的</del>，那就是JSP，JSP长的和html大差不差，区别是可以写java语句，就写在`<% %>`中，然后注释变成了`<%-- --%>`，感觉就像`JSX`和`html`的关系。JSP其实最后还是会转化为Servlet执行 —— JSP引擎将JSP文件转换为一个Servlet，然后编译并执行该Servlet

## MVC
MVC（Model-View-Controller） 是一种软件设计模式，广泛用于开发用户界面和应用程序架构。它将应用程序分为三个核心组件：Model（模型）、View（视图） 和 Controller（控制器）。这种分离有助于管理复杂性、提高代码的可维护性，并支持并行开发。