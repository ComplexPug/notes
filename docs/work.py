import os

paths = [
    "./编程语言/C++", "./编程语言/Java", "./编程语言/Python",
    "./编程语言/Lua", "./编程语言/Go", "./编程语言/Rust",
    "./编程语言/JavaScript", "./计算机科学/操作系统", "./计算机科学/计算机网络",
    "./计算机科学/计算机组成原理", "./计算机科学/数据结构和算法", "./计算机科学/软件工程",
    "./计算机科学/数据库原理", "./计算机科学/编译原理", "./计算机科学/人工智能",
    "./工具/写作工具/LaTeX", "./工具/写作工具/Markdown", "./工具/静态网页",
    "./工具/编辑器", "./工具/工具链", "./web开发",
    "./人工智能", "./DevOps", "./Books",
    "./八股", "./数据库", "./Stack","./Source Code",
    "./Source Code/Nginx",
    "./Source Code/Redis",
    "./Source Code/mkdocs",
    "./Source Code/LinuxKernel",
    "./Source Code/Minix",
    "./Source Code/fastjson",
    "./Source Code/netty",
    "./Source Code/python"
]

    

files = [
    "./编程语言/C++/note.md", "./编程语言/Java/note.md", "./编程语言/Python/note.md",
    "./编程语言/Lua/note.md", "./编程语言/Go/note.md", "./编程语言/Rust/note.md",
    "./编程语言/JavaScript/note.md", "./计算机科学/操作系统/note.md", "./计算机科学/计算机网络/note.md",
    "./计算机科学/计算机组成原理/note.md", "./计算机科学/数据结构和算法/note.md", "./计算机科学/软件工程/note.md",
    "./计算机科学/数据库原理/note.md", "./计算机科学/编译原理/note.md", "./计算机科学/人工智能/note.md",
    "./工具/写作工具/LaTeX/note.md", "./工具/写作工具/Markdown/note.md", "./工具/静态网页/note.md",
    "./工具/编辑器/note.md", "./工具/工具链/note.md", "./web开发/note.md",
    "./人工智能/note.md", "./DevOps/note.md", "./Books/note.md",
    "./八股/note.md", "./数据库/note.md", "./Stack/note.md",
    "./Source Code/Nginx/note.md",
    "./Source Code/Redis/note.md",
    "./Source Code/mkdocs/note.md",
    "./Source Code/LinuxKernel/note.md",
    "./Source Code/Minix/note.md",
    "./Source Code/fastjson/note.md",
    "./Source Code/netty/note.md",
    "./Source Code/python/note.md"
]

# 创建目录
for path in paths:
    os.makedirs(path, exist_ok=True)

# 创建文件
for file in files:
    with open(file, 'w') as f:
        f.write("# Add your notes here\n")

print("文件夹和文件创建完成。")
