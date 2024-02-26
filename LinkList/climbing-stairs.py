# https://leetcode.cn/problems/climbing-stairs/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china

class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 1
        pre = 0
        for _ in range(n):
            temp = curr
            curr = curr + pre
            pre = temp
        return curr


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))
