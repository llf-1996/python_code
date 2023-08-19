import threading
import time


LOCK = threading.Lock()
n = 0


def job1():
    global n
    for i in range(3):
        # LOCK.acquire()
        time.sleep(1)
        n += 1
        # print('job1', n)
        # LOCK.release()


def job2():
    global n
    for i in range(3):
        # LOCK.acquire()
        time.sleep(1)
        n += 10
        # print('job2', n)
        # LOCK.release()


if __name__ == '__main__':
    tt = time.time()
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(time.time() - tt)
