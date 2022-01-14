def reverse_number(x):
    """
    :type x: int
    :rtype: reversed number
    """
    reverse = 0
        
    while(x != 0):
            
        remainder = x % 10
            
        reverse = reverse * 10 + remainder
        x //= 10
            
    return print(f'The reversed number is:{reverse}')

reverse_number(123)
            
            
            