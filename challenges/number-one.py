# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.


# Example 1:

# Input: n = 13
# Output: 6
# Example 2:

# Input: n = 0
# Output: 0

# Source: Leetcode
# Must run in O(logn) time

## Brute force: Convert n to string, (string to list), iterate over string checking if n==1 and inccrement counter
### Complexity: O(nlogn), n for iteration, logn for converting n to string...
# Converting integer to list (not required):n_list = map(int, str(n))



class Solution:
    def countDigitOne(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        count = 0
        while n > 0:
            
            for i in str(n):
                if int(i) == 1:
                    count += 1
            n -= 1
        
        return count


#Next step: Optimize the algorithm to run in O(logn) time using mathematics tricks.


