# docker

## 简介

摘自官方文档：Docker is an open platform for developing, shipping, and running applications.

docker主要用于运维，当然了，开发也可以用，可以在启动应用项目的时候使用docker方式，docker是虚拟化技术，每一个docker容器都是一个linux虚拟机，而且还可以根据不同的应用定制，最小的可以直接依赖linux内核，仅仅几M就可以运行。

Docker 并非是一个通用的容器工具，它依赖于已存在并运行的 Linux 内核环境。Docker 实质上是在已经运行的 Linux 下制造了一个隔离的文件环境，因此它执行的效率几乎等同于所部署的 Linux 主机。因此，Docker 必须部署在 Linux 内核的系统上。如果其他系统，比如Windows想部署 Docker 就必须安装一个虚拟 Linux 环境。

## Docker Images

镜像是一种轻量级、可执行的独立软件包，用来打包软件运行环境和基于运行环境开发的软件，它包含运行时某个软件所需要的所有内容所需的所有内容，包括代码，库，环境变量和配置文件等。

常用指令：

1. 获取镜像```docker pull```
2. 查看镜像```docker images```或者```docker image ls```
3. 启动镜像```docker run```
4. 删除镜像```docker rmi```

## Docker Container

容器是打包代码及其所有依赖环境项的软件的标准单元，因此应用程序可以从一个计算环境快速可靠地运行到另一个计算环境。镜像在运行时会成为容器。

常用指令：

1. 查看容器```docker ps -a```
2. 启动和停止容器```doker start/restart/stop/kill```
3. 进入容器```docker exec```
4. 退出容器```exit```
5. 删除容器```docker rm id```
