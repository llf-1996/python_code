def reverse_str(data: str) -> str:
    data = list(data)
    length: int = len(data)
    for i in range(length // 2):
        data[i], data[length - i - 1] = data[length - i - 1], data[i]
    data = ''.join(data)
    return data


if __name__ == '__main__':
    data = 'abcdefg'
    res = reverse_str(data=data)
    print(res)
