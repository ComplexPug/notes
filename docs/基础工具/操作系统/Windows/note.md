# Windows

win11右键菜单自定义
    - 商店下载Custom Context Menu
Chrome开始hdr后截图曝光
	在chrome地址栏输入chrome://flags/
	在页面的搜索栏搜索force color profile
	在选项中选择所对应的颜色管理。（推荐P3

```shell
systeminfo
```

## VPN-tun 开启热点

一种就是在电脑上开启热点分享，将我们的代理服务通过热点的形式分享出去，下面将介绍如何在开启了tun模式的情况下使用。

首先进入设置-网络和Internet-移动热点开启热点，然后进入控制面板\网络和 Internet\网络连接，这时候会看到一个以Local Area Connection开头的新网卡，记住这个名字。

然后进入tun模式添加的显卡，邮件属性，进入共享选项卡，开启共享，同时指定网卡为上面新添加的网卡即可。

## windows subsystem for linux
### 快捷键
全屏:F11 or alt+shift
分屏：不如tmux
### 
/etc/rsolv.conf
wsl连接windows的ip地址
### VPN
在 Clash for Windows 中开启 TUN Mode 直接就能用了（开启前先安装好 Service Mode）

在[MicroSoft Learn](https://learn.microsoft.com/zh-cn/windows/wsl/)中有讲解

而且在wsl中安装的linux可以在windows命令行中加上wsl前缀直接使用
```
文件结构
查看系统占用空间
    wsl.exe --system -d Ubuntu-20.04 df -h /mnt/wslg/distro
导出
    wsl --export centos7 centos7.tar
导入
    wsl --import centos7 C:\centos7 centos7.tar
启动指定发行版  
    wsl -d centos7
指定用户启动
    wsl -d ubuntu -u root
文件路径转换
    # wsl路径转换为windows路径
    > wslpath -w "/mnt/c/Program Files (x86)/Steam/steamapps"
    C:\Program Files (x86)\Steam\steamapps

    # windows路径转换为wsl路径
    > wslpath "C:\Program Files (x86)\Steam\steamapps"
    /mnt/c/Program Files (x86)/Steam/steamapps
开机自启
    sudo vim /etc/wsl.conf
        [boot]
        command = service docker start

修改默认用户为root (WSL2和Windows11)
    sudo vim /etc/wsl.conf
        [user]
        default = root

互相访问
    wsl 里运行windows 程序
        # 运行windows里的python
        py.exe update_gitee_pages.py
        # open dir in wsl by windwos-sublime-text4
        alias subl subl.exe
        # 打开资源管理器
        explorer.exe .
    windows里运行wsl程序
        wsl -d ubuntu sudo bash -c "apt update"
        wsl里访问windows路径
        cd /mnt/c/Users/iuxt/Desktop
        windows 里访问wsl文件
        \\wsl$\Ubuntu\home\iuxt
```
