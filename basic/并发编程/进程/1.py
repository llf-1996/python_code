import multiprocessing
import time
from multiprocessing import Pool, Lock, Process, Manager, freeze_support
import os

LOCK = Lock()
# LOCK = Manager().Lock()


def task_with_lock(x, lock):
    print(111111, os.getpid())
    res = lock.acquire()
    print('acquire', res)
    time.sleep(3)
    lock.release()
    print('release')
    return x * x


def task_without_lock(x):
    print(f'enter ff: {os.getpid()}')
    time.sleep(3)
    print('end ff')
    return x * x


def demo_process():
    t1 = time.time()
    print(t1)
    for i in range(3):
        Process(target=task_with_lock, args=(i, LOCK)).start()
    print(time.time() - t1)


def demo_pool():
    t1 = time.time()
    print(t1)
    pool = Pool()
    for i in range(3):
        pool.apply_async(task_without_lock, (i,))
    pool.close()
    pool.join()
    print(time.time() - t1)


if __name__ == '__main__':
    # freeze_support()
    demo_process()
    demo_pool()
