# Linux

## 发行版

目前来看，我对发行版的对比一般只有包管理，自己比较常用的有Arch和Ubuntu，尤其是arch，基本什么都可以安装，工作那就有啥用啥。


上下箭头可以通过CTRL+n/p代替，适用于shell和某些时候的vim。


## common

```shell
systemctl # 守护进程
sysctl # 内核参数
```

## no-common 

```shell
# 永久关闭蜂鸣器
sudo vim /etc/modprobe.d/blacklist.conf
# 输入
blacklist pcspkr
```

## systemctl

```shell
# 常用
systemctl disable/enable <serive-name>
systemctl stop/start <serive-name>
systemctl status <serive-name>
# 查看serive，状态为active
systemctl list-units --type=service --state=active 
```

## NetworkManager

```shell
nmtui
nmcli
```


