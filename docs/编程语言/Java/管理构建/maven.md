# Maven
一个JAVA工具，用来管理项目
## 使用
windows：
    添加path
    修改conf：镜像和仓库位置
    idea修改默认maven--setting--搜索maven
### 安装
    sudo apt install maven
    mvn -v 查看版本信息
    pom.xml 项目描述文件
    没有的jar包会联网下载。
    下载过本地会备份，下次就不用下了。
### 构建命令/生命周期
三大阶段不讲了。
```
mvn compile
mvn clean   
mvn test    
mvn package 
mvn install #安装到本地仓库
```
### 需要会的
    全局配置和用户配置
    修改远程仓库位置
    修改本地仓库位置

### 间接依赖
如果不想依赖可以排除依赖
依赖范围 scope，可以选择在主程序，测试程序，打包，中是否存在

