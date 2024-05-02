# Docker
## 概念
Docker 包括三个基本概念:
镜像（Image）：Docker 镜像（Image），就相当于是一个 root 文件系统。比如官方镜像 ubuntu:16.04 就包含了完整的一套 Ubuntu16.04 最小系统的 root 文件系统。
容器（Container）：镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的类和实例一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。
仓库（Repository）：仓库可看成一个代码控制中心，用来保存镜像。
Docker 使用客户端-服务器 (C/S) 架构模式，使用远程API来管理和创建Docker容器。
Docker 容器通过 Docker 镜像来创建。
容器与镜像的关系类似于面向对象编程中的对象与类。
## 安装
看官网
不知道为什么，windows和wsl都安装了docker，结果是互通的
```bash
重启docker服务
sudo systemctl restart docker
sudo service docker restart
```
## 构建镜像 Dockerfile

## Commands
```
<name> = <name> or <hash-id>
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
    -p 端口映射
    --name
    -d 后台运行
    -e 设置环境变量
    --restart: 设置容器的重启策略。例如，--restart always将确保容器在退出时总是重启。
    -it: 这个选项实际上是两个选项的组合：-i（交互模式）和 -t（分配一个伪终端）。这对于当你需要进入容器进行交互操作（如使用bash shell）时非常有用。
    --network: 指定容器使用的网络。这对于配置容器间的网络通信非常重要。
    --rm: 告诉Docker在容器停止后自动删除它。这对于不需要持久保留的临时容器非常有用。
    -m 或 --memory: 限制容器使用的内存量。
    --cpus: 分配CPU资源。你可以指定容器可以使用的CPU核心数量。
    -v 或 --volume: （前面已提及）用于挂载卷，但也可以用于匿名卷和具名卷的创建。
    --link: 允许容器相互通信，这在Docker引入自定义网络之前非常常用。
    --expose: 暴露容器的端口或端口范围，仅在使用链接（--link）时有效。
docker logs <name>
docker stop <name>
docker stop $(docker ps -q) 停止所有容器
docker rm <name>
docker container prune 删除所有停止的容器
docker ps [-a -q]  a是all,q是quiet,查看容器
docker restart <name> 重启正在运行的容器
docker start <name> 启动容器
docker exec -it <name> <path> /bin/bash 命令行模式进入容器的路径(/bin/bash是启动命令)
docker pull mysql:5.7 下载镜像
docker update <name> --restart=always 开机自启

run         Create and run a new container from an image
exec        Execute a command in a running container
ps          List containers
build       Build an image from a Dockerfile
pull        Download an image from a registry
push        Upload an image to a registry
images      List images
login       Log in to a registry
logout      Log out from a registry
search      Search Docker Hub for images
version     Show the Docker version information
info        Display system-wide informationv
```
## 安装mysql
mysql的默认版本是Oracle linux版本
首先明白逻辑。docker中安装mysql，挂在本地目录到容器，本地用navicat或者datagrip连接，实现同步。
### Commands
```
docker exec -it <name> /bin/bash
docker run --name mysql_guli -d  -p 3306:3306 \
-v C:\Users\30106\Desktop\gulimall\mydata\mysql\log:/var/log/mysql \
-v C:\Users\30106\Desktop\gulimall\mydata\mysql\data:/var/lib/mysql \
-v C:\Users\30106\Desktop\gulimall\mydata\mysql\conf:/etc/mysql/conf.d \
-e MYSQL_ROOT_PASSWORD=123456 \
-d mysql:8.0.36-debian

参数说明
-p 3306:3306：将容器的 3306 端口映射到主机的 3306 端口
-v /mydata/mysql/conf:/etc/mysql：将配置文件夹挂载到主机
-v /mydata/mysql/log:/var/log/mysql：将日志文件夹挂载到主机
-v /mydata/mysql/data:/var/lib/mysql/：将配置文件夹挂载到主机
-e MYSQL_ROOT_PASSWORD=root：初始化 root 用户的密码
```
里面没有ssh，需要的话需要先安装openssh-server
### 连接数据库
jetbrain-datagrip
或者小熊猫
## 安装redis
### Commands
```
docker exec -it <name> redis-cli
docker run -p 6379:6379 --name redis_guli -v C:\Users\30106\Desktop\gulimall\mydata\redis\data:/data -v C:\Users\30106\Desktop\gulimall\mydata\redis\conf\redis.conf:/etc/redis/redis.conf -d redis redis-server /etc/redis/redis.conf
```
-d是后台执行
redis是版本
redis-server /etc/redis/redis.conf是执行的命令
创建的时候，挂载要提前建立好文件，不然就会变成文件夹
   
docker run --name mysql -d  -p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=123456 \
-d mysql:8.0.36-debian


docker run -p 6379:6379 --name redis -d redis redis-server
## Dockerfile
FROM 这个镜像的妈妈是谁? (指定基础镜像)
AINTAINER 告诉别人，谁负责养它?(指定维护者信息，可以没有)
RUN 你想让它干啥 (在命令前面加上RUN即可)
ADD 给它点创业资金 (COPY文件，会自动解压)
WORKDIR 我是cd,今天刚化了妆 (设置当前工作目录)
VOLUME 给它一个存放行李的地方 (设置卷，挂载主机目录)
EXPOSE 它要打开的门是啥 (指定对外的端口)
CMD 奔跑吧，兄弟! (指定容器启动后的要干的事情)
#指定基础镜像，一切从这里构建
FROM
#镜像是谁写的，姓名+邮箱
AINTAINER
#镜像构建运行时需要运行的命令
RUN
#添加的内容
ADD
#指定镜像的工作目录
WORKDIR
#指定挂载的容器卷
VOLUME
#指定暴露的端口
EXPOSE
#指定容器启动时要运行的命令，只有最后一个会生效，可被替代
CMD
#指定容器启动时要运行的命令，可以追加命令
ENTRYPOINT
#当构建一个被继承的DockerFile，这个时候就会运行ONBUILD指令
ONBUILD
#类似ADD，将文件拷贝进镜像中
COPY
#构建的时候设置环境变量
ENV

# Wrong
## 关于安装平台
我在wsl中安装了docker，然后想远程连接上，结果端口搞死我了。
其实没必要在wsl中安装docker，其实docker哪里不都一样吗
## Exited(1)
exit(1)的问题，有时候容器启动了直接是exit(1)了，检查容器和宿主的关联文件夹是否清空。
检查关联文件夹是否清空了！！！！
## 端口连接不上
检查端口是否被占用了
## MySQL
MySQL的很多版本都是OracleLinux的，没见过的话:贼坑，以为是超简化版的linux。
