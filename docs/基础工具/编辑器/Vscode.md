# VsCode
## ShortCut
alt+z 对一行很长的字符，多行表示一行

对于 行 的操作：
重开一行：光标在行尾的话，回车即可；
                 不在行尾，ctrl + enter 向下重开一行
	ctrl+shift + enter 则是在上一行重开一行删除一行：
光标没有选择内容时，ctrl + x 剪切一行；
ctrl +shift + k 直接删除一行移动一行：
alt + ↑ 向上移动一行；
alt + ↓ 向下移动一行复制一行：
shift + alt + ↓ 向下复制一行；
shift + alt + ↑ 向上复制一行
ctrl + z 回退对于 词 的操作：
选中一个词：ctrl + d 
搜索或者替换：ctrl + f ：
搜索ctrl + alt + f： 
替换ctrl + shift + f：
在项目内搜索通过Ctrl + ` 可以打开或关闭终端
Ctrl+P 快速打开最近打开的文件
Ctrl+Shift+N 
打开新的编辑器窗口
Ctrl+Shift+W 关闭编辑器
Ctrl + Home 跳转到页头
Ctrl + End 跳转到页尾

## Markdown的图片保存路径问题
vscode在2023年的时候内置了快速粘贴剪切版的视频，图片。
对于图片，如果想改变保存位置，需要到扩展里面的MarkDown里面修改Markdown › Copy Files: Destination。或者在setting.json加上，具体的一些路径宏在注释里面。
```json
"markdown.copyFiles.destination": {
  "*.md": "${documentDirName}/.assert/${fileName}"
}
```