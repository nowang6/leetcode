#https://leetcode.cn/problems/container-with-most-water/description/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            if height[left] < height[right]:
                res = max(res, height[left]*(right - left))
                left +=1
            else:
                res = max(res, height[right]*(right - left))
                right -=1
        return res

if __name__ == '__main__':
    s = Solution()
    l = [1,2,1]
    print(s.maxArea(l))
