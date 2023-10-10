def binary_search(datas, target):
    length = len(datas)
    if length == 0:
        return -1
    left = 0
    right = len(datas) - 1
    while left <= right:
        mid = (left + right) // 2
        if datas[mid] == target:
            return mid
        elif datas[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    datas = [1, 2, 3]
    target = 1
    res = binary_search(datas, target)
    print(res)
