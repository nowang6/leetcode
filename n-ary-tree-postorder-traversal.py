#https://leetcode.cn/problems/n-ary-tree-postorder-traversal/
from typing import Optional, List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root:
            for child in root.children:
                res.extend(self.postorder(child))
            res.append(root.val)
        return res
