# MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Install
需要Python环境
```shell
pip install mkdocs
```
注意，如果安装完成后没有mkdocs，可以使用sudo命令安装或者虚拟环境安装。 

## Theme
theme内置了两个mkdocs和readthedocs，其他的主题可以通过pip安装，所以会比较all in doc一点，我喜欢
可以查看  material,terminal等主题。meterial的使用量比较多。

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.
* `mkdocs gh-deploy --clean` - push gh-pages branch to GitHub

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
    site/         # The static pages.
        ...