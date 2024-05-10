# make
用来解释Makefile文件（这里使用GNU make，当然还有别的）。
可以自动化选择编译哪些文件，可以跑不止c++的代码。
## 格式
```
target: dependencies
    commands

target: file1.cpp file2.cpp
    g++ -o target file1.cpp file2.cpp
```
注意这里是依赖，而不是参数，依赖关系应该是个DAG（有向无环图）。
## 变量

变量在使用时需要加上美元符号（`$`）和括号，例如：
```
# 这是一个注释行
CC=g++
# CFLAGS 是传递给编译器的选项。
CFLAGS= -c -Wall

all: prog

prog: main.o factorial.o hello.o
	$(CC) main.o factorial.o hello.o -o prog

main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp

factorial.o: factorial.cpp
	$(CC) $(CFLAGS) factorial.cpp

hello.o: hello.cpp
	$(CC) $(CFLAGS) hello.cpp

clean:
	rm -rf *.o

```

## 自动推导

make的隐含规则

## 
c
.PHONY表示clean是一个伪目标文件

## 内部宏
这些是 make 中预定义的。
使用 make -p 列出当前构建的所有宏、后缀规则和目标

## 动态更新

```
app : main.o kbd.o command.o
    gcc -o app main.o kbd.o command.o
main.o : main.c defs.h
    gcc -c main.c
kbd.o : kbd.c defs.h command.h
    gcc -c kbd.c
command.o : command.c defs.h command.h
    gcc -c command.c
clean :
    rm app main.o kbd.o \
    command.o
```
## cmake
构建make的工具

## 资料
- [ ] [bilibili](https://www.bilibili.com/video/BV1gf4y1P7GX/?spm_id_from=333.788&vd_source=2ae0b3d86625359b9f3be85ab7c6e76e)
[GNU Make 使用手册（中译版）](https://file.elecfans.com/web1/M00/7D/E7/o4YBAFwQthSADYCWAAT9Q1w_4U0711.pdf)
[A Short Introduction to Makefile](https://www3.nd.edu/~zxu2/acms60212-40212/Makefile.pdf)
http://www.uinio.com/Linux/CMake/
[跟我一起写 Makefile](https://seisman.github.io/how-to-write-makefile/Makefile.pdf)