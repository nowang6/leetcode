# https://leetcode.cn/problems/sliding-window-maximum/

from typing import List
import queue

class MyVale:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return self.value >= other.value
    
    def __gt__(self, other):
        return self.value < other.value
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(0, len(nums)-k+1):
            q = queue.PriorityQueue(k)
            for num in nums[i:i+k]:
                q.put(MyVale(num))
            res.append(q.get().value)
        return res


nums = [1,3,-1,-3,5,3,6,7]
s = Solution()
res = s.maxSlidingWindow(nums,3)
print(res)