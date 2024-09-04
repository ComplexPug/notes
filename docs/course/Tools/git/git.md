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

git rebase xxx : 当前分支合并到xxx，等价于git rebase xxx HEAD
git rebase A B : 将B移动到A后面，也就是把B合并到A
git merge xxx：合并出新的commit
分离头指针，就是HEAD不指向branch了，
^是parent，～x是x级祖先
git branch -f 《branch name》 commit-id 更改branch指向
git reset HEAD^1 删除HEAD的commit(删除直到遇到commit-id)，是真的删除，小心使用,本地分支
git revert commit-id 撤销到某个commit，通过新建commit。远程分支
git cherry-pick 摘桃子接到head后面,cherry-pick 可以将提交树上任何地方的提交记录取过来追加到 HEAD 上（只要不是 HEAD 上游的提交就没问题）。
git rebase -i(--interactive) HEAD~4 交互式的rebase四个commit
组合技能-修改某个commit：通过rebase -i将需要改的移动到最后，commit --amend然后再rebase -i调整回去
组合技能-修改某个commit：通过cherry-pick将需要改的移动到最后，commit --amend然后再cherry-pick调整回去
HEAD是指不到远程分支的，切换会自动分离
git fetch 单纯的下载操作，不会修改本地分支
git pull = git fetch +  git merge origin/main
git pull --rebase
git push冲突的时候需要fetch，merge更新到最新，然后再push，fetch+merge=pull

git commit
    --amend
    -a
    --all
    -am
    -m

git cherry-pick

git gc

git pull
    --force
    --rebase

git fakeTeamwork

git clone

git remote
    -v

git fetch
    --force

git branch
    -d
    -D
    -f
    --force
    -a
    -r
    -u
    --contains

git add

git reset
    --hard
    --soft

git revert

git merge
    --no-ff
    --squash

git merge
    --delete-after-merge

git rev-list

git log

git show

git rebase
    -i
    --solution-ordering
    --interactive-test
    --aboveAll
    -p
    --preserve-merges
    --onto

git status

git checkout
    -b
    -B

git push
    --force
    --delete
    -d

git describe

git tag
    -d

git switch
    -c
    --create
    -C
    --force-create

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
cat .git/HEAD 等价于  git symbolic-ref HEAD
HEAD 当前分支
config 配置信e
refs 
objects 包含了commit、tree、  blob的结构内容和相互关系,HASH需要加上文件夹的两个字母

## 分离头指针 detached HEAD
git branch <new-branch-nam> <commit-name> 如果想保存修改就新建分支
## 远程仓库
先让我们添加一个远程仓库：
$ git remote add origin https://github.com/StudyingFather/my-code
$ git remote [-v]# 显示当前所有远程仓库
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


git branch -d <branch-name> 删除本地的git分支
git branch --set-upstream-to origin/newbranch 与远程分支关联
git branch -a 查看所有分支
git branch -r 列出所有远程分支
git branch 列出所有本地分支
git branch -m <旧名字> <新名字> 修改分支名
git branch [branch-name] 新建一个分支，但依然停留在当前分支

本地仓库的代码还未被更新，此时：
git fetch --all 更新远程仓库的代码为最新的
git reset --hard origin/master 让本地代码与origin / master完全相同

git checkout -b <branch> 新建一个分支，并切换到该分支
git checkout -- <filenames> 撤销文件修改，回滚到暂存区或者HEAD（优先暂存区）。
git checkout <branch-name>	切换到分支
git checkout main 切换回main分支
git checkout <commit-hashcode> /path/to/file git回滚文件到指定版
git checkout HEAD^ /path/to/file 回滚到上一个版本

git merge [branch] 合并指定分支到当前分支

删除远程分支
git push origin --delete [branch-name] 
git branch -dr [remote/branch]

git fetch 更新索引
git reset –hard 6e52	回退到某个ID
git add -u	将删除操作也添加到暂存区
git rm –cached filename	将暂存区的文件移出暂存区

根据commitid来回滚
git log /path/to/file

使用 git reset 回退项目版本
git reflog查看命令历史
git reset --hard <commit-hashcode>
    git reset --hard HEAD^


git remote add origin https://github.com/iuxt/test.git 上传，并关联到master分支
git push -u origin master 合并代码
git checkout master
git merge dev            # 将dev代码合并到master
合并方式如果是fast-forward模式, 表示git只是切换了一下指针

删除分支, 分支改名

git push --delete origin oldbranch 删除远程分支
git push origin newbranch 将重命名后的分支推到远端

# 如果远程已经删除了分支, 本地还没更新, 可以使用
git fetch -p
rebase
利用rebase删除历史提交记录
git rebase -i <你要基于那个提交的id>
commit前面的pick改成d即可，表示丢弃这个commit，如果需要推送到远端的话，需要git push -f
注意：多人协作慎用git push -f


-----------------------------------------------------------
（如果在写自己的代码过程中发现远端GitHub上代码出现改变）
git pull origin master(main) 将远端修改过的代码再更新到本地
git rebase main 我在xxx分支上，先把main移过来，然后根据我的commit来修改成新的内容
（中途可能会出现，rebase conflict -----》手动选择保留哪段代码）
git push -f origin xxx 把rebase后并且更新过的代码再push到远端github上
（-f ---》强行）
原项目主人采用pull request 中的 squash and merge 合并所有不同的commit
----------------------------------------------------------------------------------------------
远端完成更新后
2.git pull origin master 再把远端的最新代码拉至本地


git rm --cached XX：将文件从仓库索引目录中删掉
git rm --cmend :附加提交到最后一个commit
git reflog：查看HEAD指针的移动历史（包括被回滚的版本）
git reset --hard HEAD^ 或 git reset --hard HEAD~：将代码库回滚到上一个版本
git reset --hard HEAD^^：往上回滚两次，以此类推
git reset --hard HEAD~100：往上回滚100个版本
git reset --hard 版本号：回滚到某一特定版本
git checkout — XX或git restore XX：将XX文件尚未加入暂存区的修改全部撤销
git remote add origin git@git.acwing.com:xxx/XXX.git：将本地仓库关联到远程仓库
git push -u (第一次需要-u以后不需要)：将当前分支推送到远程仓库
git push origin branch_name：将本地的某个分支推送到远程仓库
git checkout -b branch_name：创建并切换到branch_name这个分支
git branch：查看所有分支和当前所处分支
git checkout branch_name：切换到branch_name这个分支
git merge branch_name：将分支branch_name合并到当前分支上
git branch -d branch_name：删除本地仓库的branch_name分支
git branch branch_name：创建新分支
git push -d origin branch_name：删除远程仓库的branch_name分支
git pull：将远程仓库的当前分支与本地仓库的当前分支合并
git pull origin branch_name：将远程仓库的branch_name分支与本地仓库的当前分支合并
git branch --set-upstream-to=origin/branch_name1 branch_name2：将远程的branch_name1分支与本地的branch_name2分支对应
git checkout -t origin/branch_name 将远程的branch_name分支拉取到本地
git stash：将工作区和暂存区中尚未提交的修改存入栈中
git stash apply：将栈顶存储的修改恢复到当前分支，但不删除栈顶元素
git stash drop：删除栈顶存储的修改
git stash pop：将栈顶存储的修改恢复到当前分支，同时删除栈顶元素
git stash list：查看栈中所有元素


git merge <branch> --squash 合并为一个commit


git branch -d <branch-name> 删除本地的git分支
git branch --set-upstream-to origin/newbranch 与远程分支关联 或者
git push --set-upstream origin branch_name：设置本地的branch_name分支对应远程仓库的branch_name分支
git branch -a 查看所有分支
git branch -r 列出所有远程分支
git branch 列出所有本地分支
git branch -m <旧名字> <新名字> 修改分支名
git branch [branch-name] 新建一个分支，但依然停留在当前分支

```

## 标签管理
```text
git tag 查看标签 
git show v1.0 查看标签详情
创建标签
切换到对应的分支, 默认是打在最新的commit上的。
git tag v1
如果想要打到历史的commit id
# 查看历史的commit id
git log --pretty=oneline --abbrev-commit
# 对 commit id 打标签
git tag v0.9 f52c633
# 打标签带上说明
git tag -a v0.1 -m "version 0.1 released" 1094adb
推送标签
# 一次性全部推送标签
git push origin --tags
# 推送一个标签到远程
git push origin refs/tags/v0.1
删除标签
# 删除本地标签
git tag -d v0.1
# 删除远程标签，需要先删除本地标签
git tag -d v0.1
git push origin :refs/tags/v0.1
```

## link

[在线练习，不错](https://learngitbranching.js.org/?locale=zh_CN)
git pro