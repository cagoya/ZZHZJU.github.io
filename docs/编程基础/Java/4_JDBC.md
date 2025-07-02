# JDBC

## 简介

Java为数据库定义了一套标准访问接口：`JDBC(Java Database Conectivity)`,JDBC接口是一套class文件，由SUN公司负责制定JDBC规范，存放在`java.sql`里面，但是这只是接口，是不能实例化的，还需要导入具体数据库的jar包。

## 流程

### 导入JDBC驱动

这里以连接MySQL为例，首先需要再项目中引入MySQL的数据驱动（我们把某个数据库实现了JDBC接口的jar包称为JDBC驱动），这个信息可以在Maven官网找到。这里设置为`runtime`的原因是编译Java程序并不需要这个包，只有在运行时才需要用到。

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.26</version>
    <scope>runtime</scope>
</dependency>
```

### 加载并注册JDBC 驱动

告诉Java程序，即将要连接的是哪个品牌的数据库，最常用反射注册

```java
Class.forName("com.mysql.cj.jdbc.Driver");
```

### 建立数据库连接

Connection代表一个JDBC连接，它相当于Java程序到数据库的连接（通常是TCP连接）。打开一个Connection时，需要准备URL、用户名和口令，才能成功连接到数据库。用完之后一定要关闭连接，因为连接数据库的开销并不小。

```java
String url = "jdbc:mysql://localhost:3306/mydatabase";
String username = "root";
String password = "password";
Connection connection = DriverManager.getConnection(url, username, password);
```

### 创建Statement对象并执行语句

JDBC提供了statement对象用于语句执行，statement对象有executeQuery方法用于SQL语句执行，返回结果保存在ResultSet对象中

```java
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery("SELECT * FROM mytable");
```

### 处理结果集

当执行的是查询操作时才有这一步骤

```java
while (resultSet.next()) {
    int id = resultSet.getInt("id");
    String name = resultSet.getString("name");
    System.out.println("ID: " + id + ", Name: " + name);
}
```

### 关闭资源

JDBC连接是一种昂贵的资源，所以使用后要及时释放

```java
resultSet.close();
statement.close();
connection.close();
```

## 重要接口和类

### DriverManger类

驱动管理类里面全是静态方法，我们用它来注册驱动：

* `static void registerDriver(Driver driver)`：向`DriverManager`注册驱动程序
* `static Connection getConnection(String url,String user,String password)`：建立到给定数据库URL的连接

### Statement类

用于指向静态SQL语句并返回结果对象：

* `int executeUpdate(String sql)`：执行更新语句，可能是`INSERT`、`UPDATE`、`DELETE`语句，返回值是数据可以中受影响的记录条数
* `ResultSet executeQuery(String sql)`：执行SQL查询语句，该语句返回单个`ResultSet`对象
* 注意列索引是从1开始。

但是JDBC中其实会**使用`PreparedStatement`**，它继承自`Statement`,允许你在 SQL 查询中使用占位符（`?`）来表示参数，使用 `setInt()`、`setString()` 等方法为占位符在运行时动态设置值,这样可以**完全避免SQL注入问题**。

### ResultSet类

用于存储查询结果：

* `boolean next()`：类似于生成器的语法，每执行一次往后移动一行，最开始在第一行之前
* `String getString(int columnindex)`：按照列的序号以字符串形式取出列，注意获取列时索引是从1开始
* `String getString(String columnLabel)`：按照列的属性以字符串形式取出列

## JDBC 事务

默认情况下，JDBC 是自动提交模式，即每个 SQL 语句都被视为一个独立的事务，执行后自动提交。要手动管理事务，需要关闭自动提交模式。大概就是把事务全部放在一个`try...catch`块中，如果抛出异常并捕获则回滚事务，否则若全部执行则提交事务。

```java
try(PreparedStatement ps = connection.preparedStatement(sql)){
    ps.excuteUpdate();
    connection.commit();
}catch(SQLException e){
    connection.rollback();
}
```
