# Cli about network 

```shell
# 修改mtu
ifconfig eth0 mtu 1472

# ip配置: nmcli，ipconfig，ip，修改配置文件（/etc/sysconfig/network-scripts）
ip address [add | del] 192.168.0.10/24 dev enp3s0
ip addr show dev enp3s0

# 默认拥塞算法

```

## netns

用来隔离网卡，注意别把ssh的网卡给隔离了，也可以隔离拥塞算法。

```shell
ip netns exec <netns-name> <command>
ip netns [add | del] <netns-name> dev <driver-interface>
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
