""" 假设你正在你的读取中读取一份文件。
你应该如何确保文件对象被正确关闭，无论是否会发生异常？这可以通过 `finally` 块来完成。"""
import sys
import time

f = None
try:
    f = open("poem.txt")
    # 我们常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()      # 立即打印到屏幕上（Windows10 没有这句也可以实现同样的效果）
        print("(Press ctrl+c now)")
        # 为了确保它能运行一段时间，设置在打印完一行后进入2秒钟的休眠
        time.sleep(2)
except IOError:
    print("!! Could not find file `poem.txt` !!")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file !!")
finally:   
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")

 # 在按下 `Ctrl + c` 后，你会注意到 `KeyboardInterrupt` 异常被抛出，尔后程序退出。
 # 不过，在程序退出之前，finally 子句得到执行，文件对象总会被关闭。


""" 关于`sys.stdout.flush()`: 
在Windows下，无论是否使用sys.stdout.flush()，其结果都是多次输出；
在Linux下，可以通过三种方式实现实时将缓冲区的内容输出：
1）sys.stdout.flush()
2）向缓冲区输入换行符，将print()的参数end设置为’\n’（其实默认 的end=’\n’）
3）将print()的参数flush设置为True（默认flush=False） """
