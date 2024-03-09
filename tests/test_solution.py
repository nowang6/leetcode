from src.Recursion.generate_parentheses import Solution
import pytest


def test_case1():
    s = Solution()
    res = s.generateParenthesis(3)
    print(res)