# -*- encoding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/5/6 14:57
# @Author  : llf
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        if q.empty():
            print('empty')
            break
        value = q.get(True)
        print('Get %s from queue.' % value)
        time.sleep(3)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    pr.join()
    # pr.terminate()  # 强行终止
