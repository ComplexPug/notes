# Arch Linux

## 特点

安装软件方便，脚本安装简单。

## 装机

制作U盘启动盘（看Arch Wiki制作）。

然后配置网络，连接wifi或者网线。（启动不了可能是网卡被禁用了）

启动后先配置国内加速镜像（直接修改mirrorlist为国内镜像，最好选一个镜像一直用），再使用archinstall自动安装。

注意：不使用加速镜像估计是安装不了。还有就是最好安装一个kde，后面不想用了可以再装别的，不然一个个下载需要的感觉上手麻烦。

## 配置

aur需要手动拉下来后再用pacman，也可以使用yay等工具来自动安装。

### 基本配置

如输入法，语言，字体等。

sshd，NetworkManager，sddm等systemctl可能也要配置一下开关。

### 日常软件

aur中的软件很齐全，配置好镜像（镜像配置在官网都有教程的）后一键安装很方面，不用一个个的网络上查找。

## 命令
```shell
# 永久关闭蜂鸣器
sudo vim /etc/modprobe.d/blacklist.conf
# 输入
blacklist pcspkr

pacman -Syyu
pacman -S <package-name> # 官方包
yay -Syyu # 更新，不同于pacman，他会更新aur
yay -R <name> # remove 
yay -Qm # 列出所有package
yay -S <package-name> # install aur包
yay -Ss <name> # 搜索包
```
