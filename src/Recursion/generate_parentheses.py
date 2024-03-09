
from typing import List
class Solution:
    res = []
    
    def recur(self, left, right, n, str):
        if left==n and right == n:
            self.res.append(str)
            return
        if left < n:
            self.recur(left + 1, right, n, str + "(")
        if right < left and right < n:
            self.recur(left, right + 1, n, str + ")")
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.recur(0, 0, n, "")
        
        return self.res
    

s = Solution()
print(s.generateParenthesis(3))