## Palindrome Permutation
# Given a string, write a function to check if it is permutation of palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.

def palindrome_permutation(stri):
    
    if stri != stri[::-1]:
        return False

    