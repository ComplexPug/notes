# Net模块
趁着实习基本改了过了一遍tcp的流程，也改了一次协议，应该可以说是协议栈开发的.
## 编译
很抓马,配置编译文件有Makefile，Kconfig，xx.config等文件。但如果直接改配置文件是很难严谨的。
`make menuconfigs`来导入.config或者查询配置变凉
```shell
make menuconfig # 帮助配置，TUI很方便。
```
## Tools
抓包工具：tcpdump，wireshark

日志工具：dmesg

热补丁：kpath等

## Command
```shell
# 内核模块命令
lsmod
insmod
```

## define
一些定义
```text
MSS MTU减去ip头和网络层头的大小
MTU 默认缺省1500，可以调整
ecn
ece
ect
tcp option：
skbuff
socket
arp

```