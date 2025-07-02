---
statistics: True
---
# 主页

<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>

<!-- 显示总访问量和访客数 -->
浏览量：<span id="busuanzi_value_site_pv"></span> |
访客数：<span id="busuanzi_value_site_uv"></span>



<center><font  color= #757575 size=6 class="ml3">“凡心所向，素履以往”</font></center>
<script src="https://cdn.statically.io/libs/animejs/2.0.2/anime.min.js"></script>

<div class="grid cards" markdown>

-   :material-notebook-edit-outline:{ .lg .middle } __导航栏__

    ---

    ![image](https://s1.imagehub.cc/images/2025/03/02/5ca6e706edd485a936961c5e8c1b6bba.webp){ class="responsive-image" align=right width="340" height="280" style="border-radius: 25px;" }

    - 𝕙𝕒𝕧𝕖 𝕒 𝕘𝕠𝕠𝕕 𝕥𝕚𝕞𝕖 !
    - <del>搜索关键词查询文章</del>
    - 如遇到无法显示图片或者$Latex$无法解析的情况，请刷新页面
    - 本站共有 {{ pages }} 个页面，{{ words }} 个字，{{ codes }} 行代码
    

</div>
<style>
    @media only screen and (max-width: 768px) {
        .responsive-image {
            display: none;
        }
    }
</style>

<style>
#rcorners3 {
  border-radius: 25px;
  border: 2px solid #518FC1;
  padding: 20px;
  width: 100%;
  height: 30%;
  font-size: 18px;
  text-align: center;
}
</style>
<body>
<font color="#B9B9B9">
  <p style="text-align: center; ">
      <span>本站已经运行</span>
      <span id='box1'></span>
</p>
  <div id="box1"></div>
  <script>
    function timingTime(){
      let start = '2024-2-26 00:00:00'
      let startTime = new Date(start).getTime()
      let currentTime = new Date().getTime()
      let difference = currentTime - startTime
      let m =  Math.floor(difference / (1000))
      let mm = m % 60  // 秒
      let f = Math.floor(m / 60)
      let ff = f % 60 // 分钟
      let s = Math.floor(f/ 60) // 小时
      let ss = s % 24
      let day = Math.floor(s  / 24 ) // 天数
      return day + "天" + ss + "时" + ff + "分" + mm +'秒'
    }
    setInterval(()=>{
document.getElementById('box1').innerHTML = timingTime()
    },1000)
  </script>
  </font>
</body>


***  


<div class="grid cards" markdown>

-   :octicons-bookmark-16:{ .lg .middle } __最近更新__

    ---

    - [ ] ZJU课程：更新大二下课程经验总结
    - [ ] 扩散模型论文阅读(持续更新)

    
-   :simple-materialformkdocs:{ .lg .middle } __个人学习计划__

    ---

    - [ ] 计算机网络
    - [ ] 操作系统
    - [ ] 深度学习

-   :material-format-font:{ .lg .middle } __好用的网站__

    ---

    
    - [CS自学指南](https://csdiy.wiki/) 
    - [ZJU-CS-ALL-IN-ONE](https://isshikihugh.github.io/zju-cs-asio/)
    - [cppperference](https://zh.cppreference.com/w/%E9%A6%96%E9%A1%B5)
    
-   :simple-aboutdotme:{ .lg .middle } __关于__

    ---

    - [关于我]()
    - 关于家乡(待写)

</div>

</head>