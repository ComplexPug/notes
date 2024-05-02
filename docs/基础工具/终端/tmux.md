# tmux教程
配置:
	配置文件放到 ~/.tmux.conf
	tmux source ~/.tmux.conf
		1.tmux下bash没有颜色
		2.鼠标设置
		3.Esc反应速度慢
		4.tmux下neovim背景色丢失，部分鼠标操作失效（暂未解决）
功能：
	(1) 分屏。
	(2) ssh远程服务断开后，继续运行进程。
结构：
	一个tmux可以包含多个session，一个session可以包含多个window，一个window可以包含多个pane。(会话，窗口，窗格）
	实例：
	tmux:
		session 0:
			window 0:
				pane 0
				pane 1
				pane 2
				...
			window 1
			window 2
			...
		session 1
		session 2
		...
操作：
  ctrl+b 是tmux的默认前缀键，操作都是由前缀键唤醒之后才能使用的
	[-s session]
	[-a attach]
	[-t target-session]

  ( ) tmux的有些调整快捷键很有意思，从触发建开始之后第一次计时，可以重复操作一小段时间。
	( ) tmux [new -s <session-name>] :新建session
	( ) tmux ls : 列出session
	( ) `tmux a [-t <session-name>]` 通过键入重新连接到tmux会话,默认是最近session
	(不如快捷键 ) tmux detach :离开session
	(不如快捷键 ) tmux rename-session testname1
	(不如快捷键 ) tmux kill-session -t <session-name> :关闭session
	(不如快捷键 ) tmux rename-window <window-name> :重命名window

  ( ) CTRL+b l :切换窗口
	( ) CTRL+b , :重命名当前窗口
	( ) CTRL+b < or >  :很奇怪的一个小窗口，类似TUI 
	( ) CTRL+b % ：将当前pane左右平分成两个pane。
	( ) CTRL+b " ：将当前pane上下平分成两个pane。
	( ) Ctrl+b d：关闭当前pane；
	( ) CTRL+b 方向键：选择相邻的pane。
	( ) Ctrl+b+方向键，可以调整pane之间分割线的位置。
	( ) CTRL+b z：将当前pane全屏/取消全屏。
	( ) CTRL+b d：挂起当前session。
	( ) CTRL+b s：选择其它session，方向键调整展开关闭。
	( ) CTRL+b c：在当前session中创建一个新的window。
	( ) CTRL+b w：选择其他window，操作方法与(12)完全相同。
	( ) CTRL+b PageUp：翻阅当前pane内的内容,Esc退出
  ( ) CTRL+b { or } : 交换pane

	( ) 鼠标操作，默认不开，点击选pane,调整大小,滚轮翻阅内容.


	(不太会用 ) 在tmux中选中文本时，需要按住shift键。（仅支持Windows和Linux，不支持Mac，不过该操作并不是必须的，因此影响不大）
	(不太会用 ) tmux中复制/粘贴文本的通用方式：
		(1) CTRL+b，然后按[
		(2) 用鼠标选中文本，被选中的文本会被自动复制到tmux的剪贴板
		(3) CTRL+b，然后按]，会将剪贴板中的内容粘贴到光标处


## config
```shell
# 颜色支持
set -g default-terminal "screen-256color"
# 鼠标支持
set -g mouse on
# ESC时间，vimESC不卡顿, can not set 0,不然启动会出现乱码，虽然无伤大雅
set -s escape-time 10

```