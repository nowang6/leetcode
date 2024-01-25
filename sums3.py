from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        length = len(nums)
        res=[]
        pre_fist = None
        for i in range(length-2):
            first = nums[i]
            if pre_fist == first:
                continue
            pre_second = None
            for j in range(i+1, length-1):
                second = nums[j]
                if pre_second == second:
                    continue
                target = -(first + second)
                if target in nums[j+1::]:
                    res.append([first,second,target])
                pre_second = second
            pre_fist = first
    
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [0,0,0]
    
    print(s.threeSum(nums))
