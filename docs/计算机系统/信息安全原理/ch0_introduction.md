# 信息安全原理
这门课主要讲了四个板块：
* Computer Security 计算机安全
* Cryptography 密码学
* Authorization and Access Control 鉴权与访问控制
* Network Security 网络安全

## 计算机安全
### Kerckhoff Principle
科霍夫原则标志着密码学从史前密码学进入经典密码学时代，它的基本假设是任何不变的东西最终都一定会被披露，加密算法本身一定会公开（比如通过逆向工程），系统的保密性只取决于秘钥本身。

如何判断一种加密方式是否符合Kerckhoff 原则？只需要关注秘钥是什么

* 太公兵符不符合Kerckhoff 原则，因为情报完全取决于算法，即根据竹简长度判断对应事件
* 豪密符合Kerckhoff 原则，秘钥是对应的那本书
* 棍子密码符合Kerhoff 原则，秘钥是棍子的直径/周长
* 隐写术不符合Kerhoff 原则，因为它们往往是一次性的算法
* ENIGMA符合Kerhoff 原则，秘钥是插线板配置、转子放置顺序和初始位置

### 计算安全三要素和攻击方式
计算机安全三要素有四个（ 分别是：
* confidential 保密性
* integrity 完整性
* available 可用性
* authetic 真实性

对应的攻击手段也有四种，假设我们的情景是A发送消息给B：
* interuption 中断：即消息在中途被阻拦，B收不到消息，破坏可用性
* interception 截取：消息确实从A发到了B，但是C也窃取到了消息内容，破坏保密性
* modification 修改：消息先从A到C，C篡改消息内容之后转发给B，破坏完整性
* fabrication 伪装：C冒充A发消息给B，破坏真实性

这里还有一组概念：
* asset 资产：我们要保护的东西
* threat 威胁：坏东西
* vulnerablity 漏洞：系统中一些未知的异常
* risk：威胁利用漏洞损害资产的概率

对抗威胁我们有三大目标：
* 预防：防患于未然
* 检测：能够及时发现问题
* 恢复：被攻击了能快速复原，更高层次追求是哪怕被攻击了也能正常工作

