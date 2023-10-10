# -*- coding: utf-8 -*-
"""
@Author: llf
@Email:
@Time: 2023/10/10
@desc: 
"""


def prime_number(start, end):
    result = []
    if start > end:
        return result
    start = 2 if start < 2 else start
    for i in range(start, end):
        # is_prime = True
        # for j in range(2, i):
        #     if i % j == 0:
        #         is_prime = False
        #         break
        # if is_prime:
        #     result.append(i)

        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


if __name__ == '__main__':
    start = 50
    end = 100
    res = prime_number(start, end)
    print(res)
