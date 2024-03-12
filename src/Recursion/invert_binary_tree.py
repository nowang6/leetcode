# https://leetcode.cn/problems/invert-binary-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      if root is None:
        return root
      left = self.invertTree(root.left)
      right = self.invertTree(root.right)
      root.left = right
      root.right = left
      return root
      



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
