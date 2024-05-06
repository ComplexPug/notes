```shell
export 
alias python="python3" # 别名

cat /etc/shells

echo $SHELL # 查看当前
exec bash # 切换shell终端

# zsh设为默认shell
chsh -s /bin/zsh
reboot

# 更新配置
source ~/.bashrc

# Bash检查当前用户是不是root
if [ $(id -u) != "0" ]; then
    echo "Error: You must be root to run this script, please use root to install lnmp"
    exit 1
fi
```

问题：有些命令在换zsh之后失效了。
解决：
原因是两个不同的终端配置不一样。
把 bash shell 中.bash_profile 全部环境变量加入zsh shell里就好
在.zshrc文件最后加上source ~/.bash_profile