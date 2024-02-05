#https://leetcode.cn/problems/merge-intervals/
from typing  import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       res = []
       intervals = sorted(intervals, key=lambda l:l[0])
       tmp = intervals[0]
       for cell in intervals[1:]:
          if tmp[1] >= cell[0]:
             tmp[1] = max(tmp[1],cell[1])
          else:
             res.append(tmp)
             tmp = cell
       res.append(tmp)
       return res

if __name__ == "__main__":
  intervals = [[1,3],[2,6],[8,10],[15,18]]
  s = Solution()
  res = s.merge(intervals)
  print(res)
