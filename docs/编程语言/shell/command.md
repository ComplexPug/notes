# Command

## base
```shell
echo # 输出
exec # 执行
export # 启动
alias python="python3" # 别名
cat # 查看，全部显示
less # 查看，但一页一页查看
echo $SHELL # 查看当前shell
exec bash # 切换shell终端
# zsh设为默认shell
chsh -s /bin/zsh
reboot
mkdir -p /a/b/c/d # 一次性创建多个目录而不是分开
pwd
find . -name 'report.pdf' 在当前目录搜索名为 report.pdf 的文件
find / -size +1G 全盘搜索大于 1G 的文件
find ~/ -name 'node_modules' -type d 在用户目录搜索所有名为 node_modules 的文件夹
source ~/.bashrc # 更新配置

# Bash检查当前用户是不是root
if [ $(id -u) != "0" ]; then
    echo "Error: You must be root to run this script, please use root to install lnmp"
    exit 1
fi

`|` 管道
`;` 当你想要无条件地顺序执行多个命令。
`&&` 当你希望只在前一个命令成功时才执行下一个命令。
`&` 后台执行    
```

问题：有些命令在换zsh之后失效了。

解决：

原因是两个不同的终端配置不一样。

把 bash shell 中.`bash_profile` 全部环境变量加入zsh shell里就好

在.zshrc文件最后加上`source ~/.bash_profile`
