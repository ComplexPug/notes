# MySQL
## Config
默认是不能远程连接的。

编辑/etc/mysql/mysql.conf.d/mysqld.cnf注释掉bind-address

```
创建账号及密码，例如创建用户admin，密码为123456

create user admin identified by '123456';
1
给最高权限 可以管理所有数据库

grant all on *.* to admin;
```