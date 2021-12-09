#### TWO SUM ####

# Given Given an array of integers nums and an integer target, 
# Return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums and i != nums.index(diff):
                return i, nums.index(diff)


### A Concise implementation (official solution) ###

class SolutionOfficial:

    def twoSum(self, nums:List[int], target:int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[num[i]] = i
            complement = target - num[i]

            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

