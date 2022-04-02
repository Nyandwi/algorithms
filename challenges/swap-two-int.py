# Given two integers, swap them with no additional variable

# 1. With temporal variable t
def swap(a,b):
    
    t = b
    a = b 
    b = t
    
    return a, b

# 2. With no variable 

def swap(a,b):
    
    a = b - a
    b = b - a # b = b -(b-a) = a
    a = b + a # b = a + b - a = b...Swapped
    
    return a, b

# With bitwise operator XOR

def swap(a,b):
    
    a = a ^ b
    b = a ^ b # b = a ^ b ^ b = a ^ 0 = a
    a = b ^ a # a = a ^ a^ b = a^a^b = b^0 = b
    
    return a, b

# Other method: just swap in place
def swap(a,b):

    a,b = b, a
    
    return a,b