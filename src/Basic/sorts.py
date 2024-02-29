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

def bubble_sort(nums:List):
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            if nums[i] > nums [j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def quick_sort(nums):
    l = len(nums)
    if(l<=1):
        return nums
    first, last, key = 0, l-1, nums[0]
    while(first < last):
        while first < last and nums[last] > key:
            last -= 1
        nums[first] = nums[last]
        while first < last and nums[first]< key:
            first += 1
        nums[last] = nums[first]
    return quick_sort(nums[0:first]) + [key] + quick_sort(nums[first+1:])



if __name__ == '__main__':
    nums = [5,4,3,2,1,10]
    nums = quick_sort(nums)
    print(nums)