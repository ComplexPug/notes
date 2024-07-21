# zsh

主要是oh-my-zsh+p10k，配置起来也很简单，不存配置文件了，用zsh主要是用提示插件。

zsh-autosugesstions插件

```shell
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# in .zshrc 
plugins=( 
    # other plugins...
    zsh-autosuggestions
)
```
