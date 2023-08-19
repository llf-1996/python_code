"""
题干:

给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


# def two_sum(nums, target):
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


def two_sum(nums, target):
    hash_table = dict()
    for i in range(len(nums)):
        if target - nums[i] in hash_table:
            return [hash_table[target-nums[i]], i]
        hash_table[nums[i]] = i


if __name__ == '__main__':
    res = two_sum([2, 7, 11, 15], 9)
    print(res)
