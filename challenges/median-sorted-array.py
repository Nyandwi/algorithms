## MEDIAN OF TWO SORTED ARRAYS
# Source: Leetcode
# Submission: Accepted

# Given two sorted arrays, nums1 and nums2,  return the medium of two sorted array. The runtime should be O(logn)
# Solution: Add two arrays, sort them, if the len of sorted array is odd, return the middle element: element at arr[n//2]
# If length of array is even, it means there are two medians, one at arr[n//2] and arr[n//2 - 1], add and divide them by two

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = nums1 + nums2
        nums_len = len(nums)
        
        sorted_nums = nums.sort()
        
        if nums_len % 2 != 0:
            return nums[nums_len//2]
        else:
            return (nums[nums_len//2] + nums[(nums_len//2 - 1)])/2

# Total runtime: O(nlogn)