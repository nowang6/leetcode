
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while r-l>1:
            mid = (l + r) // 2
            if nums[l] < nums [mid] < nums[r]:
                return nums[l]
            if nums[l] < nums [mid]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])
            
s = Solution()
nums = [11,13,15,17]
res = s.findMin(nums)
print(res)
