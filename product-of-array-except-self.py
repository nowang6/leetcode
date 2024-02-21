# https://leetcode.cn/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left_product = right_product = 1
        for i in range(n):
            res[i] = res[i] * left_product
            left_product *= nums[i]
        for i in range(n-1, -1, -1):
            res[i] = res[i] * right_product
            right_product *= nums[i]
        return res
        


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4]
    print(s.productExceptSelf(nums))
