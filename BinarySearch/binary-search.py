# https://leetcode.com/problems/binary-search


class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            if target == val:
                return mid
            elif target < val:
                r = mid -1
            else:
                l = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [5]
    target = 5
    print(s.search(nums, target))
    
