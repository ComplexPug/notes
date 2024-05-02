# MyBatis
简化JDBC(java数据库连)开发
## 使用
1.打开springboot工程
2.引入mybatis依赖
3.编写sql语句

## sql
```sql
#是预编译的，没有注入问题
select * from table where #{id}
$是拼接，有注入问题
select * from table where ${id}
```
## 动态sql
用xml来写
1.<if> 
2.<where>
3.<set> 1,2,3用来拼接
4.<sql> 片段
5.<include> 引入片段
