# Cli about network 

```shell
# 修改mtu
ifconfig eth0 mtu 1472

# ip配置: nmcli，ipconfig，ip，修改配置文件（/etc/sysconfig/network-scripts,这个最无脑，但不一定生效）
ip address [add | del] 192.168.0.10/24 dev enp3s0
ip addr show dev enp3s0
ifconfig eth0 192.168.1.4 netmask 255.255.255.0

# getway
route add default gw 192.168.1.1

# dns
vim /etc/resolv.conf


# 默认拥塞算法修改

```

## scapy


## tcpdump

[tcp flags in tcpdump](https://gist.github.com/tuxfight3r/9ac030cb0d707bb446c7)

```shell
tcpdump -l | tee pkt.log # 不记得是不是l了，反正你要刷新缓冲,不过这种方法不推荐
tcpdump -w pkt.cap # 可以存储cap格式，用wireshark解析，比直接输出到file好用的多
```

## wireshark
过滤语法其实我也不太会,可能和lua差不多
以用lua自定义显示

## netns

用来隔离网卡，注意别把ssh的网卡给隔离了，也可以隔离拥塞算法。

```shell
ip netns exec <netns-name> <command>
ip netns [add | del] <netns-name>
ip netns set <dev-name> netns <netns-name>
ip netns list
```

## iperf3

网络压力测试

```shell
iperf help
-s server
-c client
指定拥塞算法只能指定客户端，有时候可能需要搭配netns修改
```

## route

## ethtool


