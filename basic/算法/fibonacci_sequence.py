# -*- coding: utf-8 -*-
"""
@Author: llf
@Email:
@Time: 2023/10/11
@desc: 斐波拉契数列
"""


def fib(max):
    n, a, b = 0, 1, 1
    while n < max:
        # print(a)
        yield a
        a, b = b, a + b
        n = n + 1
    return 'done'


if __name__ == '__main__':
    for i in fib(10):
        print(i)
