
#https://leetcode.cn/problems/house-robber
class Solution(object):
    def rob(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]



if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,1]
    #[2,7,9,3,1]

    print(s.rob(nums))
    