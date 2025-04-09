# TypeScript
## 简介
TypeScript是微软基于JS构建的一种强类型的语言，强制执行严格的类型检查，所以TS包含JS

具体而言就是在定义变量的时候可以给定一个类型，就像是C语言的`int`，比如
```ts
let message: string = "hello";
message=1;//会报错，因为类型不匹配
```
还有数组也是同理
```ts
let array: string[] = ["a","b","c"];
```
ts甚至还提供了枚举变量
```ts
enum Color {
    Red,
    Green,
    Blue
}
```
## 增加的语法
### 接口
相当于C++中的抽象类，比如
```ts
interface User{
    _id: string;
    name: string;
    is_admin?: boolean;// ?表示可选项
}

const user: User={
    _id: "123",
    name: "shihao"
}
```
这个也是可以继承的，不过叫做extend interface，比如
```ts
interface Shape{
    color: "blue" | "green" | "red";
}

interface Circle extends Shape{
    radius: number;
}
```

### 字面类型
允许指定一个变量只能取特定的字面量值
```ts
type flexDirection = "row" | "column";
```

### 字面函数
```ts
interface Comment {
    id: string;
    text: string;
    author: string;
}

const getComments = (id: string): Comment[] => {
    return []; // 目前返回空数组
}

```