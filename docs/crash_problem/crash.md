- [x] mysql root登录不进去
```shell
vim /etc/my.cnf 跳过验证
[mysqld]
skip-grant-tables

然后修改密码再关闭skip
```
