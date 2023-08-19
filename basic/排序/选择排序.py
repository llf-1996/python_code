def select_sort(datas):
    for i in range(len(datas) - 1):
        min_index = i
        for j in range(i + 1, len(datas)):
            if datas[j] < datas[min_index]:
                min_index = j
        datas[i], datas[min_index] = datas[min_index], datas[i]
    return datas


if __name__ == '__main__':
    datas = [1, 5, 2, 7, 4]
    res = select_sort(datas)
    print(res)
