# ### 一、选择题
#
# 1. 在 Python 中，以下关于进程和线程的说法，正确的是（ C ）
#
# A. 进程之间共享内存空间，线程之间不共享      B. 创建进程比创建线程开销更小
#
# C. 一个进程可以包含多个线程      D. 线程不能并发执行，进程可以并发执行
#
# 2. 以下哪个模块用于在 Python 中创建进程？（  B）
#
#    A. threading  B. multiprocessing	C. os	D. sys
#
# ### 二、编程题
#
# 1. 使用multiprocessing模块创建两个进程，一个进程打印从 1 到 5 的数字，另一个进程打印从 6 到 10 的数字。
import  multiprocessing

def pro1():
    for i in  range(1,6):
        print(i)

def pro2():
    for i2 in range(6,11):
        print(i2)

pro1()
pro2()
# if __name__ == '__main__':
#     p1=multiprocessing.Process(target=pro1)
#     p2=multiprocessing.Process(target=pro2)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

# 2. 使用threading模块创建两个线程，一个线程打印 10 次 "Hello"，另一个线程打印 10 次 "World"。
