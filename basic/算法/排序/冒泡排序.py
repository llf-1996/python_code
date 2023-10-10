from typing import List


def bubble_sort(datas: List):
    for i in range(len(datas) - 1):
        for j in range(len(datas) - i - 1):
            if datas[j] > datas[j+1]:
                datas[j], datas[j+1] = datas[j+1], datas[j]
    return datas


if __name__ == '__main__':
    datas = [1, 4, 2, 3, 9]
    res = bubble_sort(datas)
    print(res)
