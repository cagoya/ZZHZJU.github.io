# `ASP.NET core` 基础
## `ASP.NET core` 概述
### SDK
SDK即Software Development Kit，中文一般叫做软件开发包，是一组工具、库、文档和示例代码的集合，用来帮助开发者更容易地开发特定平台或服务上的应用程序。这里需要用到`.NET`的SDK

### .NET
`.NET`是一个通用的开发平台，可以运行多种语言编写的程序，其中`C#`是最常用的语言，它提供了：
* 一套运行时(.NET runtime)和一些语言支持：`C#、VB.NET、F#` 等
* 基础类库（Base Class Library, BCL），比如：文件操作、网络、集合、LINQ 等
* 一个统一的工具链（编译器、NuGet、调试器等）

.NET 支持开发多种类型的应用，包括但不限于Web应用，移动平台应用等

### `ASP.NET core`
`ASP.NET`是一个Web框架，`ASP.NET core`是它的重新设计，`ASP.NET core`相比`ASP.NET`格局有重大根本性改变，可以直接在VS中用`web api`模版创建一个web 应用，各文件/文件夹的内容大概如下：
* Controller:里面是api控制器类，负责处理HTTP请求，并返回响应结果
* Properties:里面是元数据，例如`lauchSettings.json`,用于配置本地运行时的环境（比如端口、调试器等设置）
* appsettings.json:配置文件，用于设置数据库连接字符串、日志级别、第三方服务信息等
* Program.cs:是程序的入口，使用 WebApplication.CreateBuilder() 来创建并配置 Web 应用
* Models/：需手动添加，定义数据类型，用于MVC架构
* wwwroot/：仅用于有前端文件的项目，需手动创建

## 控制器
首先所有控制器都应该继承自`ControllerBase`，这样才会有`Ok()`这些方法

### 属性
`[ApiController]`一般任何一个控制器都要添加，加上能使控制器获得如下特性：
* 如果请求体中的数据模型验证失败（比如缺失必填字段、格式错误等），控制器会自动返回 400 Bad Request，不需要你手动写验证逻辑。
* 更智能的参数推断，但是还是不建议省略`[FromBody]、[FromQuery]、[FromRoute]`等属性
* 当返回值为 ActionResult<T> 时，如果你返回了 null，系统会自动返回 404 Not Found，而不是 204 No Content
* 错误会以 JSON 格式自动返回给客户端，包含详细的字段错误信息

处理不同的HTTP请求只需要添加一个`[HttpGet]`，`[HttpPost]`之类的属性，还可以加参数来指定具体路径，还可以加别名，比如```[HttpGet(Name = "GetWeatherForecast")]```,主要用于在其他地方通过名字引用这个路由，所以名字可以随便取

``` csharp
// 路由同一页面多个GET请求的例子
[ApiController]
[Route("api/[controller]")]
public class ProductController : ControllerBase
{
    // GET: api/product
    [HttpGet]
    public IActionResult GetAllProducts()
    {
        return Ok("获取所有产品");
    }

    // GET: api/product/5，打括号表示直接是这个变量名的值
    [HttpGet("{id}")]
    public IActionResult GetProductById(int id)
    {
        return Ok($"获取ID为 {id} 的产品");
    }

    // GET: api/product/byname?name=apple
    [HttpGet("byname")]
    public IActionResult GetProductByName(string name)
    {
        return Ok($"获取名称为 {name} 的产品");
    }
}

```

[Route("[controller]")]表示路由路径为控制器文件名去除`Controller`，可以实现路径自动同步

### 参数
某些参数来自HTTP请求，比如`[FromBody]`告诉框架这个参数应该从 HTTP 请求的 Body（请求体）中读取并进行反序列化，这个就比Java智能多了，Java本身甚至没有处理json的库，此外还有[FromQuery]来自URL查询参数，[FromForm]来自表单

### 返回值
`Task<ActionResult>`是`ASP.NET Core` Web API 中定义控制器方法返回类型的一种写法，`Task`说明这个方法是异步执行的，可以在里面使用`await`，`ActionResult`说明返回值是一个HTTP响应,比如：
* Ok()（200）
* NotFound()（404）
* BadRequest()（400）
* Created()（201）
* NoContent()（204）

## 模型
其实就是存储需要的信息的类，比如可以有一个模型表示保存在数据库里的条目，有时候也称为一个记录(entity)

可以用`[Required]`来标注必须填写的字段

`Guid`（global unique identifier）即全局唯一标识符，是一个由数字和字母组成的长长的字符串

## 视图
`ASP.NET core`里面的视图使用`Razor`模版语言编写，这种模版语言混合了`HTML`和`C#`，`C#`需要用`@`作为前缀

## 依赖注入
在 Program.cs 里面添加需要注入的依赖
比如：
```csharp
//在
builder.Services.AddSingleton<Service>();
```
之后无论在哪个控制器或服务中注入 Service，它们获得的都是同一个实例（Id 值相同）
