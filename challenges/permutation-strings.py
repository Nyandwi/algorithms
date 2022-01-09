### Given two strings, determine whether one is permutations of the other
# Solution: Two strings are permutations of each other if they have the same characters in different order. 
# So, you can sort them and compare them
# Clarify if they are case sensitive, or if they contain space. 

# Answer 1: Brute force, sort and compare

def permutation_str(str1, str2):

    if sorted(str1) == sorted(str2):
        return True

# Concise answer 2:

