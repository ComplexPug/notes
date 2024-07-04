# Notes

手感外观界面都挺好的，不过触控板感觉也不是很惊艳，还是喜欢鼠标一点，键盘也不错，pro的手感比air好一点。

不是很喜欢，可能用win+Linux更舒服一些。

## 备份

时间机器。相当于快照。建议磁盘大小是两倍存储（应该可以选择某些不快照，后面弄）。

## 软件安装

网上下载的可执行软件可以拖动到启动台。

homebrew ： 包管理

tmux

oh-my-zsh：git,autosuggestions

iterm2 : 代替terminal，终端软件，安装oh-my-zsh

乱码问题：[powerline](https://github.com/powerline/fonts)

KeyCastr : 将mac按键显示在屏幕上，分享演示、录制视频或动图.

Obs :


vim：在里面的粘贴体验很棒，是我用过最好的。

pstree：没有

对于gdb，gcc等Linux工具确实比较难安装（尤其是gdb）。我觉得比较said，但和win对比一下跨平台也能理解，如果在win上用vs不就直接ide了，至少mac还是全替换了。

## 软件卸载

控制台摁下option键盘

或者用访达删除文件夹

## 终端

cmd+k 或者ctrl+l ：真正的clear
clear只是位移

## 虚拟机
Parallels Desktop ： 收费，懒得折腾
utm ： 简单，官网免费
virtual box ： 貌似开发热情不高，只有开发版且不常更新
vmare ： 个人免费，下载有点难找

## 手势
四指聚拢 : 打开启动台

四指张开 : 显示桌面 

其他的都是一些和win类似的

注：crxMouse in chrome会影响右键等操作。

## 快捷键
[官网快捷键说明](https://support.apple.com/zh-cn/102650)
如果是中文输入法下，有些快捷键会不起作用。

### vscode
command+shifit+z 取消撤回
option + 上下 移动一行  + 左右 单词移动
command + 左右 begin/end

### 其他

contrl,option,command

给屏幕拍照。Shift-Command-3 拍摄整个屏幕的图片。Shift-Command-4 拍摄屏幕上你选择部分的图片。

command + 左/右 : home和end

control + 点摁 : 右击

control + 上下 : 三指上下
control + 左右 : 三指左右

复制file后粘贴的时候用 option+command+v 就剪切了.

command更像是win的ctrl，类似于复制粘贴，chrome快捷键都是用command

command + , : 打开当前软件设置

control + command + f : 全屏软件

control + 左右： 切换桌面

contrl + space : 切换输入法

大写键其实默认是中英切换，ctrl + 切换键是大写键

command + space : 聚焦搜索

option + command + c : 复制finder当前路径

option + 启动台 ： 删除不是App Store的软件
option + 全屏按钮 ：默认的三个（左，右，全）都是全屏操作，点击option都被替换为当前桌面的操作 

F11 显示桌面

fn + backspace ： delete

fn + F : 退出/进入全屏

command + i ： 显示详细信息

command + 上下 ： 进入进出文件夹（回车是修改名字）

command + 删除 ： 可以删除文件

`open <path>` 访达打开文件夹
## 兼容性

移动硬盘不能使用ntfs，需要exfat。

对于Linux的一些工具链，gdb，gcc，pstree的替代品基本不想用（不想学第二遍）