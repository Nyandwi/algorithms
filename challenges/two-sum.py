#### TWO SUM ####

### 1st Method

#Source:leetcode

# Given Given an array of integers nums and an integer target, 
# Return indices of the two numbers such that they add up to target.
def two_sum(arr, target):
    """
    Given a sorted array, return the indices of the two elements such that they add up to the target sum.

    To solve it:
    Take the last element(high) in the array and compare it with the rest of the elements in the array. 
    If the sum of the two elements is equal to the target, return the indices of the two elements.
    """
    
    n = len(arr)
    high = arr[-1]
    index_1 = 0
    index_2 = 0
    
    for i in range(n):
        if arr[i] + high == target:
            index_1 = i
            index_2 = arr.index(high)

    return index_1, index_2

arr = [1,3,4,5]
            
i1, i2 = two_sum(arr, 9)
print(f"{i1}, {i2}")

Runtime: O(logn)

# 2nd Method: COMPLIMENT METHOD

def two_sum_2(arr, target):
    """
    Given an array and target, return two indices of values that add up to target
    Answer: Loop through the array, subtracting target to every value...
    If the values exists, the difference of target and i and summation to arr[i]...
    Should be equal to target. 
    """

    n = len(arr)

    for i in range(n):
        comp = target - arr[i]
        
        if comp in arr and arr[i] + comp == target:
            return i, arr.index(comp)

#runtime: Linear, O(1)


### A Concise implementation (official solution) ###

class SolutionOfficial:

    def twoSum(self, nums:List[int], target:int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[num[i]] = i
            complement = target - num[i]

            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

