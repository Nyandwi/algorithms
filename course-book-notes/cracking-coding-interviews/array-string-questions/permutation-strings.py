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
    Count the occurence of each individual character in each string.
    If the counts are the same, the strings are permutations of each other.

    Counts are stored in array of 128 size. This is an assumption that we are using ASCII characters. 
    The number of characters in ASCII is 128. 
    """
    if len(s1) != len(s2):
        return False

    count_s1 = [0] * 128
    for char in s1:
        count_s1[ord(char)] += 1

    count_s2 = [0] * 128
    for char in s2:
        count_s2[ord(char)] += 1
    
    if count_s1 == count_s2:
      return True
    else:
      return False

## There is something off in the implementation: Solved 
# Test the algorithm on many inputs strings: It works

## Testing the algoritm on different inputs
#string_permutation('foo','ofo')
## Output: True

#string_permutation('foo','hhdnd')
## Output: False

#string_permutation('foo','gbf')
## Output: False

#string_permutation('foo','fcd')
#Output: False

#string_permutation('foo','fog')
## Output: False
