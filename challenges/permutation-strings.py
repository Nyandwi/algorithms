### Given two strings, determine whether one is permutations of the other
# Solution: Two strings are permutations of each other if they have the same characters in different order. 
# So, you can sort them and compare them
# Clarify if they are case sensitive, or if they contain space. 

# Answer 1: Brute force, sort and compare

def permutation_str(str1, str2):

    if len(str1) != len(str2):
        return False

    if sorted(str1) == sorted(str2):
        return True

# Concise answer 2: Count the number of individual characters in each string 
## and compare the counts. 

def string_permutation(s1,s2):
    """
    Edge case: If the strings are not the same length, they are not permutations of each other.
    """
    if len(s1) != len(s2):
        return False

    count = [0] * 128
    for char in s1:
        count[ord(char)] += 1

    for char in s2:
        count[ord(char)] -= 1
        if count[ord(char)] < 0:
            return False
        return True

## There is something off in the implementation. 
# Test the algorithm on many inputs strings. 
