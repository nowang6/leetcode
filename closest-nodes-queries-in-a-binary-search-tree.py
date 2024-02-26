# https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math
from typing import List, Optional

class Solution:
    def build_tree_from_array(self, nums):
        length = len(nums)
        if length == 0:
          return None
        root = TreeNode(nums[0])
        index, pre_level = 1, [root]
        tree_level_depth = math.ceil(math.log(length,2))
        for level in range(1,tree_level_depth):
            level_size = 2 ** level
            curr_level = []
            for i, element in enumerate(nums[index:index+level_size]):
                node = TreeNode(element)
                curr_level.append(node)
                pre_index = i // 2
                if i%2 == 0:
                    pre_level[pre_index].left = node
                else:
                    pre_level[pre_index].right = node
            index += level_size
            pre_level = curr_level
        return root
    
    def bfs(self, root):
        nums = []
        if root is None:
            return nums
        nums.extend(self.bfs(root.left))
        val = root.val
        if val is not None:
          nums.append(root.val)
        nums.extend(self.bfs(root.right))
        return nums
    
    def middle_search(self, nums, left, right, target):
        if left == right:
            val = nums[left]
            if target < val:
              if left == 0:
                return [-1, val]
              else:
                return [nums[left-1], val]
            else:
              if right == len(nums) - 1: 
                return [val, -1]
              else:
                return [val,nums[right+1]]
        mid_index = (left + right) // 2
        mid_val = nums[mid_index]
        if target == mid_val:
            return [target, target]
        elif target < mid_val:
            return self.middle_search(nums,left,mid_index-1,target)
        else:
            return self.middle_search(nums,mid_index+1,right,target)
            
        
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        tree_root = self.build_tree_from_array(root)
        nums = self.bfs(tree_root)
        res = []
        for q in queries:
            res.append(self.middle_search(nums,0, len(nums)-1, q))
        return res

null = None
nums = [6,2,13,1,4,9,15,null,null,null,null,null,null,14]
queries = [2,5,16]
s = Solution()
res = s.closestNodes(nums,queries = [2,5,16])
print(res)
