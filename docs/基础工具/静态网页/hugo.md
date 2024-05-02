# Hugo
一款用go编写的静态网页生成器。
可以类比hexo。
## Base
基本上配置好只有几个常用命令
```
hugo new post/path/name.md
hugo server -D
# 对于name.md的命名，用-分割即可，hugo会自动转化大小写，比如try-in-work的title会是"Try in Work"
```
## common command
```
hugo new site MyFreshWebsite --format yaml 新建站点
hugo version 查看版本
hugo server -D 本地预览，修改配置是不需要重启的
hugo 构建网站
hugo env 环境信息
hugo new post/xxx.md 创建文章
hugo list 
hugo help 查看帮助

--bind="127.0.0.1"    服务监听IP地址；
-p, --port=1313       服务监听端口；
-w, --watch[=true]      监听站点目录，发现文件变更自动编译；
-D, --buildDrafts     包括被标记为draft的文章；
-E, --buildExpired    包括已过期的文章；
-F, --buildFuture     包括将在未来发布的文章；
-b, --baseURL="www.datals.com"  服务监听域名；
--log[=false]:           开启日志；
--logFile="/var/log/hugo.log":          log输出路径；
-t, --theme=""          指定主题；
-v, --verbose[=false]: 输出详细信息
```
## config
评论的话需要细琐，还未实现
静态页面的逻辑还是比较简单的。
主题放到themes文件夹下即可（有很多种方式）
配置要在hugo.yaml下配置
```yaml
menu.main 下的weight是排序权重
params.mainSections下可以存发布文件夹，默认只有一个最多。
theme: <theme-name>
# 中文魔改模板
languageCode: zh
defaultContentLanguage: zh

```
archives搜索文档wiki创建
其他的就照葫芦画瓢，看theme的wiki修改。

## Front Matter
什么是Front Matter，就是markdown文章的头部的
```markdown
+++
title = 'T3'
date = 2024-02-24T21:14:00+08:00
draft = false
weight = 10 weight越小越top
+++
```

## themes
[PaperMod](https://github.com/adityatelange/hugo-PaperMod/)

