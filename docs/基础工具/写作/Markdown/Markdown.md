## mkdocs material
!!! note "这是 note 类型的提示框"
提示：更多精彩内容记得关注我啊

!!! success "这是 success 类型的提示框"
成功！

!!! failure "这是 failure 类型的提示框"
失败！

!!! bug "这是 bug 类型的提示框"
发现一个 bug，请尽快修复！

??? note "这是 note 类型的提示框"
提示：更多精彩内容记得关注我啊

## 选择
css
文本编辑器
notion
印象笔记
one-note
Obsidian
vscode
typora
flomo
memos

## Markdown Base

### 标题

在 Markdown 中，一共有 6 级标题。

| 标题     | 用法          |
| -------- | ------------- |
| 一级标题 | `# 标题`      |
| 二级标题 | `## 标题`     |
| 三级标题 | `### 标题`    |
| 四级标题 | `#### 标题`   |
| 五级标题 | `##### 标题`  |
| 六级标题 | `###### 标题` |

### 加粗

\*`**test**`，即有**test**。正常打出\*只需要转义一下`\*`

### 斜体

输入`*test*`，即有*test*。

### 插入链接

`[google](https://www.google.com/)`，即有[google](https://www.google.com/)。

### 插入代码

 “\`” 将你希望作为行内代码的内容包围起来即可。

`` ``` ``,`printf("Hello, world!");`

```` `` ``` ``,`printf("Hello, world!");` ````

````` ```` `` ``` ``,`printf("Hello, world!");` ```` `````

对于想输出`` ` ``的问题，不够就加左右的`` ` ``。

### 代码块

````
```python
print("hello world")
```
````

```python
print("hello world")
```

### 引用

输入`> hello`。

>   hello

### 分割线

输入`------`

------

### todo
```
- [x] 吃饭
- [x] 睡觉
- [ ] 学习
```
- [x] 吃饭
- [x] 睡觉
- [ ] 学习

### 表格

```
|  UserId | UserName     |   DepartmentId              |
| ------: | :----------- | :-------------------------: |
|  12     | Li hua       |     12545448484548444       |
|  234433 | Xiao Ming    |     545455450054212         |
```
可以看出`:`可以控制左对齐右对齐和居中对齐。
|  UserId | UserName     |   DepartmentId              |
| ------: | :----------- | :-------------------------: |
|  12     | Li hua       |     12545448484548444       |
|  234433 | Xiao Ming    |     545455450054212         |

### 列表

#### 无序列表

用`- `列出

```markdown
- test1
- test2
- test3
```

即有如下效果：

- test1
- test2
- test3

#### 有序列表

用形如`1. `列出

```markdown
1. test1
2. test2
3. test3
```

即有如下效果：

1. test1
2. test2
3. test3