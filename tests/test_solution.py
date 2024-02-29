from src.Tree.closest_nodes_queries_in_a_binary_search_tree import Solution
import pytest



def test_case1():
    null = None
    nums = [16,8,18,1,12,null,20,null,2,9,null,null,null,null,7]
    queries = [8,14,285508,6]
    s = Solution()
    res = s.closestNodes(nums,queries = [2,5,16])
    print(res)