# git
## 基础
Working Directory 工作目录
Stage(Index) 暂存区
History(Repository) 所有commit和branch
Branch 分支
Commit
Romote Repository 远程仓库
HEAD 指向最后一次提交的指针,本质还是个commit
## SSH公钥配置步骤
1.本地安装好git；
2.桌面右键 Git Bash Here 打开git命令行；
3.ssh-keygen -t rsa -C “xxxxxx@xxx.com” (这个写自己注册时的邮箱)（全部按enter）；
4.cd ~/.ssh （如果没有执行第三步，则不会有这个文件夹）；
5.cat id_rsa.pub 在命令行打开这个文件，会直接输出密钥；
6.复制，打开github ，点自己头像 >> settings >> SSH and GPG keys >>New SSH key
## Branch 分支
分支有很多默认名称
master --> 转向main
origin
main
## 配置
1.配置用户信息
    git config --global user.name "your name"
    git config --global user.email "name@abc.com"
    发现user.name有多个值:
    git config --global --replace-all user.email "输入你的邮箱" 
    git config --global --replace-all user.name "输入你的用户名"
2.配置分支默认值为main
    git config --global init.defaultBranch main

3.缺省值为local
    --local 对某个仓库有效
    --global 对当前用户所有仓库有效 
    --system 对所有登陆系统用户有效

4.显示config的配置 --list
    git config --list --local
    git config --list --global
    git config --list --system
    git config --list --local [user.name]

5.默认编辑器
    git config --local editor vim

6.设置代理
    # 端口
    git config --global http.proxy 127.0.0.1:7890
    git config --global https.proxy 127.0.0.1:7890
    # 取消代理
    git config --global --unset http.proxy
    git config --global --unset https.proxy
    # 查看代理
    git config --global --get http.proxy
    git config --global --get https.proxy
7.记住密码
git config --global credential.helper store
## Git Command
git init [<dir-name>]
git add/rm files
git commit -m <file>
git commit -am "ajbc" 工作区到History
git status
git log [--all] [--graph] [--oneline]一个版本一行 [-n4]最近四个
git restore --staged 
git reset --hard
git mv readme readme.md //其实直接操作git也会改逻辑为mv
git branch -va 查看分支
git checkout -b temp 版本号 切换分支
git help --web log  查看git log帮助
git cat-file -t 版本号 查看版本号的类型
git cat-file -p 版本号 查看版本号的内容
    tree 包含一些blob
    commit 包含一些blob和tree，tree类似文件夹
    blob 文件
    tag
git checkout -b <new-branch-name> <branch-name or commit>
git diff <commit1> <commit2> HEAD也是一个commit
HEAD^1^1 or HEAD^^1 OR HEAD~2 HEAD的父亲的父亲
版本号只需要能唯一区别出来即可，不必全部输入
git branch -d <branch-name> 删除分支
git branch -D <branch-name>
git branch -av :查看分支 
git branch --amend 修在最新的commit的message的分支
git rebase -i <commit> 修改旧的commit的message、合并commit（不连续或者连续）
git diff --cached 暂存区和HEAD的区别
git diff 工作区和暂存区的区别
git diff -- <files> 查看工作区和暂存区的file文件的差异
git reset HEAD 暂存区恢复到HEAD
git reset  工作区恢复到暂存区
checkout 工作区变动
reset 暂存区
git checkout  
    
## .git
HEAD 当前分支
config 配置信e
refs 
objects 包含了commit、tree、  blob的结构内容和相互关系,HASH需要加上文件夹的两个字母
    
## gitk
一个简单的可视化git工具，小巧一点。
## 分离头指针 detached HEAD
HEAD不指向任何分支，工作在没有分支branch的情况下，更改没有基于branch，切换别的brach之后有可能会被git当作垃圾删掉。
git checkout <commit-name> 分离
git branch <new-branch-nam> <commit-name> 如果想保存修改就新建分支
## HEAD and branch
HEAD总是落脚于一个commit
## Part 4.6 远程仓库
我们可以将我们对仓库的修改提交到远程仓库（例如托管在 Github 上的仓库）。
先让我们添加一个远程仓库：
$ git remote add origin https://github.com/StudyingFather/my-code
$ git remote # 显示当前所有远程仓库
origin
移除远程仓库也很容易：
$ git remote rm origin
当我们在远程仓库作出一些更改时，需要将这些更改拉取到本地时，请使用 `git fetch` 命令。
$ git fetch origin # 将 origin 上的修改拉取到本地
需要注意，执行完 git fetch 命令后，只会抓取数据而不会合并，合并工作需要自己完成。
要想在抓取的同时将远程仓库的进度和本地合并，可以使用 git pull 命令。
$ git pull origin master # 抓取 origin 的数据并自动和本地的 master 分支合并
当我们完成了修改，使用`git push`命令可以将修改推送至远程仓库。
$ git push origin master # 将 master 分支的数据推送至 origin
在推送更改时，需要注意下面几点：
如果是第一次向远程仓库推送修改，Git 会要求输入远程仓库的账号和密码。
和分支合并类似，当远程分支有新更改而当前分支没有时，推送操作会失败。这时请执行 git pull 命令完成合并再提交。


