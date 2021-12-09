# Given an integer x, return True if the integer is a palindrome number
# A palindrome number is a number that can be read the same way from left to right


def is_palindrome(x):
    """
    >>> is_palindrome(121)
    True
    >>> is_palindrome(123)
    False
    """
    return str(x) == str(x)[::-1]

is_palindrome(121)

#### A Concise Solution

def palindrome(x)
    # Return a quick false if x < 0
    # Also if the last number is 0, the first has to be 0 too. 
        
    if (x < 0 or (x % 10 == 0 and x != 0)):
        False
        
    reversed_number = 0
        
    while(x > reversed_number):
            
        reversed_number = reversed_number * 10 + x % 10
        x /= 10
            
    return x == reversed_number or x == reversed_number/10

"""
The Algorithm behind the code above:
1. If x is less than 0, return immediate false since it is not a palindrome.
2. If the last number of x is 0, then the first number has to be 0 too. 
3. How to reverse a number: 
    a. For a number 1221, if we do 1221 % 10, we get the last number 1,
    b. If we remove 1 from 1221 by 1221/10=122 and we do 122 % 10, we get the second number 2,
    c. If we multiply the last digit by 10 and add the second digit, we get 1 * 10 + 2 = 12. This is the reversed number that we wanted
    d. Continue the process until all numbers are reversed:
    e. Just simple: You do mudular 10 and keep the remainder (it is the first reversed digit)
    .... and divide the number by 10 to get to remove the last digit that were reversed

"""

            