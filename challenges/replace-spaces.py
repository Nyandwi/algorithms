
# Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the "true" length of the string. 
# (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)
# Example: 
# Input: "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

def replace_spaces(str, true_length):
    return str.replace(' ', '%20')

# Testing the function

str_1 = 'Mr John Smith    '
str1_replaced = replace_spaces(str_1, 13)
print(str1_replaced)
#Output: Mr%20John%20Smith%20%20%20%20

# The above output is half correct. The correct output should be Mr%20John%20Smith.
# The spaces at the end of the string are merely for holding any additional characters.
# These additional spaces should not replaced with %20.

def replace_string_2(str, true_length):
    """
    Given a string and a true length of the string, replace all spaces with %20.
    Be careful with the spaces that comes after the last character. 
    
    Solution: Count the spaces in the string[:true_length] and add 2*count to the true_length...
    ...when returning the string.
    """

    space_count = 0
    for char in str[:true_length]:
        if char == ' ':
            space_count += 1 

    str_2 = str.replace(' ', '%20')
    return str_2[:true_length + space_count * 2]

str_2 = 'Mr John Smith    '
str2_replaced = replace_string_2(str_2, 13)
print(str2_replaced)
#Output: Mr%20John%20Smith

str_3 = 'Mr John             '
str3_replaced = replace_string_2(str_3, 7)
print(str3_replaced)

str_4 = 'Mr Set                 '
str4_replaced = replace_string_2(str_4, 6)
print(str4_replaced)

#Output: Mr%20John
# Great, but can I do better? Perhaps without using the replace method?



