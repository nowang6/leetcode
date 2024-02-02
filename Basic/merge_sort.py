from typing import List

def merge(left:List, right:List):
    res = []
    i = j = 0
    while i<len(left) and j<len(right):
        if (left[i]<=right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def merge_sort(nums: List):
    n = len(nums)
    if n <= 1:
        return nums
    mid = n // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left,right)


if __name__ == '__main__':
    nums = [5,4,3,2,1,10]
    nums = merge_sort(nums)
    print(nums)