def quicksort(array):
    if len(array) < 2:
        return array
    point_index = 0
    point_data = array[point_index]
    less_part = [i for i in array[point_index+1:] if i <= point_data]
    more_part = [i for i in array[point_index+1:] if i > point_data]
    return quicksort(less_part) + [point_data] + quicksort(more_part)


if __name__ == '__main__':
    import random

    array = list(range(10))
    random.shuffle(array)
    print('before:', array)
    res = quicksort(array)
    print('after:', res)
