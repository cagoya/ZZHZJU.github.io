# 关于我

<html lang="en">
<p style="text-align: center; margin: 0px;" markdown>
  <img src="https://s1.imagehub.cc/images/2025/01/21/a747a42434c92c8b596ec5fd6923c5ab.png" alt="arv-anshul" style="width: 300px; border-radius: 50%;" />
  <p style="text-align: center; font-size: 30px; margin: 0px;"><strong>A college student in Hangzhou</strong></p>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
        <link rel="stylesheet" href="../assets/stylesheets/portfolio.css">
    </head>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>统计展示</title>
    <style>
        /* 全局基础样式 */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            background-color: #f9f9f9; /* 页面背景色 */
        }

        .main {
            padding: 50px 0;
        }

        .about__info {
            display: flex; /* 水平排列 */
            justify-content: space-around; /* 项目等间距 */
            align-items: center; /* 垂直居中对齐 */
            margin-top: 20px;
        }

        .about__info-item {
            text-align: center; /* 居中对齐 */
        }

        .about__info-title {
            font-size: 2rem; /* 数字的字体大小 */
            font-weight: bold;
            color: #08BF9B; /* 设置数字的颜色 */
            display: block;
        }

        .about__info-name {
            font-size: 1rem; /* 文字的字体大小 */
            color: #333333;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <main class="main">
        <section class="about section" id="about">
            <div class="about__container container">
                <div class="about__data">
                    <div class="about__info">
                        <div class="about__info-item">
                            <span class="about__info-title">00+</span>
                            <span class="about__info-name">工作经验</span>
                        </div>
                        <div class="about__info-item">
                            <span class="about__info-title">02+</span>
                            <span class="about__info-name">已经完成的项目</span>
                        </div>
                        <div class="about__info-item">
                            <span class="about__info-title">00+</span>
                            <span class="about__info-name">贡献的开源</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
</body>
</html>


---

## 教育经历

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>时间轴效果</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }

        .timeline {
            position: relative;
            max-width: 600px;
            margin: 0 auto;
        }

        .timeline::after {
            content: '';
            position: absolute;
            width: 4px;
            background-color: #08ADBF;
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -2px;
        }

        .timeline-item {
            position: relative;
            padding: 20px 40px;
            width: 50%;
        }

        .timeline-item.left {
            left: 0;
            text-align: right;
        }

        .timeline-item.right {
            left: 50%;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            width: 20px;
            height: 20px;
            background-color: #fff;
            border: 4px solid #08ADBF;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            border-radius: 50%;
            z-index: 1;
        }

        .timeline-item.left::before {
            left: auto;
            right: -10px;
        }

        .timeline-item.right::before {
            left: -10px;
        }

        .timeline-content {
            background-color: #fff;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #ddd;
            text-align: center;
        }

        .timeline-content h3 {
            margin-top: 0;
            color: #08ADBF;
        }

        .timeline-content p {
            margin: 5px 0 0;
        }

        .timeline-content .date {
            font-size: 0.9em;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="timeline">
        <div class="timeline-item left">
            <div class="timeline-content">
                <h3>四川省德阳中学</h3>
                <p>初高中六年</p>
                <p class="date">2017 - 2023</p>
            </div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content">
                <h3>浙江大学</h3>
                <p>软件工程学士(ing)</p>
                <p class="date">2023 - 2027</p>
            </div>
        </div>
        <div class="timeline-item left">
            <div class="timeline-content">
                <h3>浙江大学（待定）</h3>
                <p>？？？</p>
                <p class="date">??? - ???</p>
            </div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content">
                <h3>未完待续</h3>
                <p>为热爱的事奔走，才不会觉得辛苦</p>
            </div>
        </div>
    </div>
</body>
</html>

## 联系我

<center>
  <img class="img1" src="https://s1.imagehub.cc/images/2025/01/21/5912ddca822c245b1c389246875cc6e4.jpg" style="width: 250px; height: auto;">
    <div style="color:orange; 
    color: #999;
    padding: 2px;">我的Wechat，不过是收款码</div>
</center>


## 须知
如果你在浏览博客的过程中发现了任何问题，欢迎评论区留言，尤其是关于某些课程的。如果你有其他事情想要咨询，可以通过下方按钮使用邮件联系我。

[Send Email :fontawesome-solid-paper-plane:](mailto:<wangkewen821@gmail.com>){.md-button}  