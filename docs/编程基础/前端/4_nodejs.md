# Node.js
## 简介
基于 Chrome V8 引擎的 JavaScript运行环境，允许开发者在服务器端使用JS，它的特点包括：
* 异步非阻塞：Node.js使用事件驱动的非阻塞I/O模型，使它能够处理大量并发请求
* 单线程：Node.js运行在单线程上，但通过事件勋魂机制实现并发处理
* 高性能：得益于V8引擎，Node.js执行JS代码的速度非常快

## 基础语法
Node.js本身就内置了一个HTTP服务器模块，也就是可以直接用node.js的HTTP模块来创建服务器，处理HTTP请求，并生成web页面。

Node.js应用由以下三部分组成：
* require模块：加载和引入模块
* 创建服务器：服务器可以监听客户端请求
* 接收请求与响应请求：客户端可以使用浏览器或中断发送HTTP请求，服务器接收请求后返回响应数据

### 创建Node.js应用
#### 使用require指令来加载和引入模块
语法格式如下：
```js
const module = require('module_name');
```

require指令会返回加载的模块的导出对象，可以通过该对象来访问模块中定义的属性和方法，比如：
```js
const http=require("http");
```

#### 创建服务器
```js
const http = require('http')

http.createServer(function(request,response){
    response.writeHead(200,{'Content-Type': 'text/plain'});
}).listen(8888);
```