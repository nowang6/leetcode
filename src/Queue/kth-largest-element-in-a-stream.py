# https://leetcode.cn/problems/kth-largest-element-in-a-stream/description/
from typing import List

import queue

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
      self.pq = queue.PriorityQueue(k)
      self.k = k
      for num in nums:
        self.add(num)         
            
    def add(self, val: int) -> int:
      if self.pq.qsize() < self.k:
        self.pq.put(val)
      elif self.pq.queue[0] < val:
        # 将要加入的值更大
        self.pq.get()
        self.pq.put(val)
      return self.pq.queue[0]   
         
k =  KthLargest(3, [4, 5, 8, 2])
k.add(3)
k.add(5)
k.add(10)
