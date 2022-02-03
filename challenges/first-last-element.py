# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        midd = n//2
        pos = []
        
        if target not in nums:
            return [-1, -1]

        if n == 1:
            return [0, 0]    
      
        if nums[midd] == target:
            pos.append(nums.index(target))
            
        if nums[midd + 1] == target:
            pos.append(nums.index(target) + 1)
        
        elif nums[midd] < target:
            searchRange(nums[:n], target)
        
        elif nums[midd] > target:
            searchRange(nums[n:], target)                                    
        
        return pos

### Error: the function is not working for list with 2 or less elements...Fix it with edge/base cases.