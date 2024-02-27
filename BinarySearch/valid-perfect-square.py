# https://leetcode.cn/problems/valid-perfect-square
import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, math.ceil(num/2)
        while l <= r:
            mid = (l + r) // 2
            square = mid ** 2
            if square == num:
                return True
            elif square < num:
                l = mid + 1
            else:
                r = mid - 1
        return False

if __name__ == '__main__':
    s = Solution()    
    print(s.isPerfectSquare(16))
