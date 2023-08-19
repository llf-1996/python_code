class Solution(object):
    def trap(self, height):
        # 动态规划
        ans = 0
        n = len(height)
        if n < 3: return 0
        maxLeft, maxRight = [0] * n, [0] * n
        maxLeft[0], maxRight[-1] = height[0], height[-1]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        for i in range(n):
            ans += min(maxLeft[i], maxRight[i]) - height[i]
        return ans


if __name__ == '__main__':
    """
    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6

    """
    datas = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = Solution().trap(datas)
    print(res)
