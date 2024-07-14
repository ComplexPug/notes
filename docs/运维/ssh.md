# ssh
 windows上会有一些好用的软件，如xshell，xftp，mobaxterm，但其他平台就不是很多了。
## ssh config
其实在vscode remote ssh的时候配置的格式就是ssh config。
```shell
Host 服务器名A
    user 用户名
    hostname 服务器ip
    port 端口号 # 默认22
    identityfile 本地私钥地址
    ...
Host 服务器名B
    user 用户名
    hostname 服务器ip
    port 端口号
    identityfile 本地私钥地址
    ...
...
...
Host *
    ...
    ...
可选
    Identityfile：指定本地认证私钥地址
    ForwardAgent yes：允许ssh-agent转发
    IdentitiesOnly：指定ssh是否仅使用配置文件或命令行指定的私钥文件进行认证。值为yes或no，默认为no，该情况可在ssh-agent提供了太多的认证文件时使用
    IdentityFile：指定认证私钥文件
    StrictHostKeyChecking：有3种选项
    ask：默认值，第一次连接陌生服务器时提示是否添加，同时如果远程服务器公钥改变时拒绝连接
    yes：不会自动添加服务器公钥到~/.ssh/known_hosts中，同时如果远程服务器公钥改变时拒绝连接
    no：自动增加新的主机键到~/.ssh/known_hosts中
```