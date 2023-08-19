from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        x = 1
        for r in range(0, n//2 + 1):
            for i in range(r, n - r):
                res[r][i] = x
                x += 1
            for j in range(r + 1, n - r):
                res[j][n-r-1] = x
                x += 1
            for k in range(n-r-2, r, -1):
                res[n-r-1][k] = x
                x += 1
            for m in range(n-r-1, r, -1):
                res[m][r] = x
                x += 1
        return res


if __name__ == '__main__':
    res = Solution().generateMatrix(5)
    print(res)

"""
[
    [1,  2,  3,  4,  5], 
    [16, 17, 18, 19, 6], 
    [15, 24, 25, 20, 7], 
    [14, 23, 22, 21, 8], 
    [13, 12, 11, 10, 9]
]


[
    [1,  2,  3,  4], 
    [12, 13, 14, 5], 
    [11, 16, 15, 6], 
    [10,  9,  8, 7]
]


"""
