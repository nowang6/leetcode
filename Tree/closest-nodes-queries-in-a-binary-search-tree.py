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

            
        
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        root = self.build_tree_from_array(root)
        nums = self.bfs(root)
        res = []
        for q in queries:
            if q < nums[0]:
                res.append([-1, nums[0]])
                break
            if q >= nums[-1]:
                res.append([nums[-1],-1])
                break
            l, r = 0, len(nums) - 1
            while (r - l ) > 1:
                mid_index = (l + r) // 2
                mid_val = nums[mid_index]
                if mid_val == q:
                    res.append([q,q])
                    break
                elif q < mid_val:
                    r = mid_index
                else:
                    l = mid_index
            if (r-l) == 1:
                res.append([nums[l], nums[r]])
        return res

null = None
nums = [16,8,18,1,12,null,20,null,2,9,null,null,null,null,7]
queries = [8,14,285508,6]
s = Solution()
res = s.closestNodes(nums,queries = [2,5,16])
print(res)
