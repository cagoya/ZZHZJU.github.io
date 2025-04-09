# Vue3
Vue是一款用于构建用户界面的渐进式JS框架，它提供了两种风格的API——选项式API和组件式API，两种风格是互通的，这里选择选项式API

## 基础
### 创建
每个Vue应用都是通过`createApp`函数创建一个新的应用实例
```js
import {createApp} from 'vue'

const app = createApp({
    /*根组件选项*/
})
```
### 挂载
应用实例必须在调用了`.mount()`方法后才会渲染出来，改方法接收一个“容器”参数，可以是一个实际的DOM元素或是一个CSS选择器字符串：
```js
<div id="app"></div>
app.mount('#app')
```
应用的根组件将会被渲染在容器元素里面，容器元素不会被视为应用的一部分。

`.mount()`方法应该始终在整个应用配置和资源注册完成后被调用，同时请注意，它返回的是**根组件实例**而非应用实例，不同于其他资源注册方法

应用实例并不只限于一个，`create`API允许你在同一个页面中创建多个共存的Vue应用，而且每个应用相互默认是独立的。

### 模版语法
Vue使用一种基于html的语法，使我们能够声明式地将其组件实例的数据绑定到呈现的DOM上。所有的Vue模版都是语法层面合法的HTML，可以被符合规范的浏览器和HTML解析器解析。

和React类似，Vue在应用变更时，能智能地推导出需要重新渲染的组件的最少数量，并应用最少得DOM操作。

双大括号会将其中的内容替换成相应组件实例中`msg`属性的值，同时，每次`msg`属性更改时它也会同步更新

```js
<span>Massage: {{msg}}</span>
```

但是这个解析的结果是纯文本，而不是HTML，要想得到HTML，需要使用`v-html`指令。这个指令由`v`开头，可以看出这是一个Vue提供的特殊`attribute`

双大括号不能再标签中使用，如果确实有需要，应该使用`v-bind`指令，这个非常常用并且提供了缩写
```js
<div v-bind:id="dynamicId"></div>
<div :id="dynamicId"></div>
```

Vue中JS表达式可以被应用在以下场景：
* 在文本插值中
* 在任何Vue指令attribute的值中

每个绑定只支持单一表达式，也就是能跟在`return`后面的，特别强调**条件控制也不支持**，<del>此事在REACT中亦有记载</del>

### 响应式基础
选用选项式API时，会用`data`选项来声明组件的响应式状态。此选项的返回值应为一个对象的函数。

要为组件添加方法，我们需要用到`methods`选项，Vue自动为`method`中绑定了永远指向组件实例的`this`。当修改了响应式状态时，DOM会被自动更新。和React一样，DOM的更新是不同步的。

如果一个有状态的方法需要复用，可以在`created`声明周期钩子中创建预置的函数。

### 计算属性
可以使用`computed`包装一个按照计算结果返回内容的函数，之后这个函数就可以作为JS对象嵌入在标签里面，与普通方法不同，计算属性值会基于其响应式依赖被缓存，一个计算属性仅会在其响应式依赖更新时才重新计算。

计算属性默认是只读的，但是在某些特殊情况下可以用`getter`和`setter`创建可写属性。

### 条件渲染
Vue提供了`v-if`进行条件渲染，同样有`v-else`和`v-else-if`，可以在`<template>`上使用`v-if`，这只是一个不可见的包装器元素，最后渲染结果并不会包含这个`<template>`元素

另外还有`v-show`，但这个仅仅是修改`display`的CSS属性，DOM中始终会渲染保留该元素。

### 列表渲染
我们可以使用`v-for`指令基于一个数组来渲染一个列表，会用到`item in items`的语法，`v-for`也支持第二个参数表示索引，和Python是一样的，并且可以完整访问父作用域内的属性和变量

### 事件处理
可以使用`v-on`指令（简写为`@`）来监听DOM事件，并在事件触发时执行对应的JS。用法：`v-on:click="handler"`或`@click="handler`。事件处理器的值可以是：
1. 内联事件处理器：事件被触发时执行内联JS语句（与`onclick`类似）
2. 方法事件处理器：一个指向组件上定义的方法的属性名或是路径

#### 内联事件处理器
通常用于简单的场景，例如：
```js
data() {
    return {
        count: 0
    }
}
```
```jsx
<button @click="count++">Add 1</button>
<p>Count is: {{count}}</p>
```
直接绑定方法名，还可以在内联事件处理器中调用方法，这允许传参以替代原生事件。有时需要访问原生DOM事件，可以向处理器方法传入一个特殊的`$event`变量

#### 方法事件处理器
`v-on`也可以接受一个方法名或对某个方法的调用
```js
data() {
    return {
        name： 'Vue.js'
    }
},
methods: {
    greet(event) {
        alert(`Hello ${this.name}!`)
        if(event){
            alert(event.target.tagName)
        }
    }
}
```
```jsx
<button @click="greet">Greet</button>
```
#### 修饰符
##### 事件修饰符
在处理事件时调用`event.preventDefault()`或者`event.stopPropagation()`是很常见的。尽管可以在方法内调用，但如果方法能更专注于数据逻辑而不用去处理DOM事件的细节会更好。为了解决这一问题，Vue提供了事件修饰符（`.`表示的指令后缀），包含以下这些：
* `.stop`
* `.prevent`
* `.self`
* `.capture`
* `.once`：最多触发一次
* `.passive`：用于触摸事件的监听器，可以用来改善移动端设备的滚屏性能

##### 按键修饰符
##### 鼠标按键修饰符

### 表单输入处理
在前端处理表单，通常需要把表单输入框内容同步给JS中相应的变量，手动连接值绑定和更改事件监听器可能会很麻烦
```js
<input
    :value="text"
    @input="event => text = event.target.value">
```

`v-model`指令可以简化这一步骤
```js
<input v-model="text">
```

多行文本可以使用
```js
<textarea v-model="message" placeholder="add multiple lines"></textarea>
```



### 侦听器
计算属性允许我们声明性地计算衍生值，然而在有些情况下，我们需要再债台变化时执行一些“副作用”：例如修改DOM，或是根据异步操作的结果去修改另一处的状态。在选项式API中，我们可以使用`watch`选项在每次响应式属性发生变化时触发一个函数。