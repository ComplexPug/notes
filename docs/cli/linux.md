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


