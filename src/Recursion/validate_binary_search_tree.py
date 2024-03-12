# https://leetcode.cn/problems/validate-binary-search-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], lower, upper) -> bool:
      if root is None:
        return True
      
      val = root.val
      if not lower<val<upper:
        return False
      
      left = root.left
      right = root.right
      left_value = left.val if left else -sys.maxsize-1
      right_value = right.val if right else sys.maxsize
      if not left_value<val<right_value:
        return False
      
      return self.helper(root.left,lower,val) and self.helper(root.right,val,upper)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      return self.helper(root, float("-inf"), float("inf"))
     



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

s = Solution()
res = s.invertTree(root)
print(res)
