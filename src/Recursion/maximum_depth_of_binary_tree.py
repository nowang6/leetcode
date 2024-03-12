# https://leetcode.cn/problems/maximum-depth-of-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      if root is None:
        return 0
      left_dep = self.maxDepth(root.left)
      right_dep = self.maxDepth(root.right)
      return max(left_dep,right_dep) + 1
     



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

s = Solution()
res = s.maxDepth(root)
print(res)
