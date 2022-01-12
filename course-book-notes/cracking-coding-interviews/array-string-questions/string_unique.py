# ## Given a string 
# ## implement an algorithm that determine if the string has unique characters

### Clarify if the string is ASCII or Unicode...
### ASCII strings has standard english letters (A-Z, a-z), digits, and numbers
### Unicode strings has all numerous characters from many languages: latin, greek, etc...


def string_unique(stri):
    """
    Given a string, determine if it has all unique characters.
    """
    if len(stri) > 128:
        return False

    char_set = [False] * 128
    for char in stri:
        val = ord(char) #ord return the unicode value of the character
        if char_set[val]:
            return False
        char_set[val] = True
    return True

string_example = "I love to code"

string_unique(string_example)

#Runtime: O(n)
# Space: O(1)

"""
If we can't use additional data structures:
>> compare every character of the string to every other character of the string. This will take O(n^2)
>> If we are allowed to modify the input string, we could sort the string in O(n log n) time and then linearly check the 
...string for neighboring characters that are identical. Be careful, many sorting algorithms may take extra space
"""





