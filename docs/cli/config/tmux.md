# Author: ComplexPug
# Path: ~/.tmux.conf

# 颜色支持
set -g default-terminal "screen-256color"
# 鼠标支持
set -g mouse on
# ESC时间，vimESC不卡顿, can not set 0,不然启动会出现乱码，虽然无伤大雅
set -s escape-time 10
# 设置大小防止名字过长显示不全
set-option -g status-left-length 100
