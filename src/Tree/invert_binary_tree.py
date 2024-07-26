#https://leetcode.cn/problems/invert-binary-tree/description/
from typing import Optional, List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
   def invertTree(self, root):
    if root:
        left = root.left
        right = root.right
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
    return root
