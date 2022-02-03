## Bit Manipulation

* To a computer, everything is a number. On its front end, it abstract us with super intuitive and good numbers and letters, but deep inside, everything is stored in `1's` and `0's`. Computers deal with binary digits or bits.

* We as humans use decimal numbers because they easier for us. We do not need to convert numbers between numbers system when counting or doing other numeric/arthmetic operations. Computers use binary system because they are easier to implement in hardware using logic gates.

* Bit manipulation is a technique used to manipulate bits or other pieces of data at the lowest level. It is mostly used in error detection and correction algorithms, control devices, data compression, encryption algorithms and optimization.

* Python has `bitwise operators` that are used to manipulate individual bits. The majority of programmers don't need to manipulate bits since that is taken by Python.

### Python Bitwise Operators

* Bitwise operators operate on operands(the data) bit by bit, hence the name `bitwise`. The normal logical operators(`nor`, `or`, `and`) are used to evaluate expressions.

* Python bitwise operators only works with integers.

* If you want to operate on bit by bit, you should not use logical operators.

* There are 6 main bitwise operators:
  * Bitwise AND: `&`
  * Bitwise OR: `|`
  * Bitwise NOT: `~`
  * Bitwise XOR: `^`
  * Bitwise left shift: `<<`
  * Bitwise right shift: `>>`

* Bitwise operators are similar across almost all programming languages. 
  
* With the exception of `Bit wise Not ~`, all other operators require two operands (`left and right operands`). Operands are data to be operated on. Example: `a & b`, `&` is `bitwise AND`, `a` is `left operand`, `b` is `right operand`.

#### Bitwise AND &

* Bitwise AND performs logical AND for all corresponding bits. It returns 1 if corresponding bits are 1 and else 0. 

Example:

```
    a = 1010 #10 in decimal
    b = 0111 #7 in decimal
#--------------
a & b = 0010 #2 in decimal
```
```python
a = 10 
b = 7
print(f"a & b: {a & b}")
```
```
a & b: 2
```

* Bitwise AND is equivalent to multiplication. If you multiply `a` and `b`, you would get the same response.

#### Bitwise OR |

* Bitwise OR performs logical OR for all corresponding bits. It returns 1 either of the corresponding bits is 1 and 0 if corresponding bits are 0.

Example:

```
    a = 1010 #10 in decimal
    b = 0111 #7 in decimal
#--------------
a | b = 1111 #15 in decimal
```

```python
a = 10 
b = 7
print(f"a | b: {a | b}")
```
```
a | b: 15
```

* Bitwise `a | b`) is equivalent to `a | b = a + b - (a x b)`. Note this is to be performed on individual bits.

#### Bitwise NOT ~

* Bitwise NOT performs negation or inversion of bits. It flips the corresponding bits where 1 become 0 and 0 become 1. 

* Bitwise NOT only operates on 1 operand. 

Example:

```
    a = 1010 #10 in decimal
#--------------
    ~a  = 0101 #5 in decimal
 ```

* The inverted bits are compliment of 1. That is to say  `~ a = 1 - a`(bit by bit).

#### Bitwise XOR ^

* Bitwise XOR `^` returns 1 if the corresponding bits are not similar and 0 otherwise.
* XOR stands for exclusive OR. The corresponding bit pair must be exclusive or opposite for it to return 1. 

Example:

```
    a = 1010 #10 in decimal
    b = 0111 #7 in decimal
#--------------
a ^ b = 1101 #13 in decimal
```
* Bitwise XOR is equivalent to the modular 2 (%) of the sum of the operands: ` a ^ b = (a + b) % 2`.

#### Bitwise Shift Operators

* Bitwise shift operators are used to shift bits left or right by a given level. We can use shift operators to multiply or divide a number by a power of 2. 
  
##### Bitwise Left Shift Operator

* Bitwise left shift operator `(<<`) shifts the bits of the number to the left by  a specified places or number of shifts. 
  
* It's like multiplying the number by the power of 2. If you are only shifting for one place, it's equivalent to doubling the number. Shifting for two spaces, it's multiplying the number by 4.
  
* The gap left pn the right after shifting on the left is filled by 0. 

* Shifting to the left is equivalent to multiplying the number by power of 2: a << n = a x 2<sup>n</sup>.


* Examples:

```
a = 1110001
a << 1 = 11100010
a << 2 = 111000100
a << 4 = 11100010000
```
```python
a = 10 
print(f"a << 3: {a << 3}")
```
```
a << 3: 80
```

##### Bitwise Right Shift Operator

* Bitwise right shift operator `(>>)` shifts the bits of the number to the right by  a specified places or number of shifts.
  
* It's like dividing the number by the power of 2. If you are only shifting for one place, it's equivalent to dividing the number by 2. Shifting for two spaces, it's dividing the number by 4.
  
* The gap left on the left after shifting to the right can be filled with 0's but it does not change anything.

* Shifting to the right is equivalent to dividing the number by power of 2: a << n = a / 2<sup>n</sup>.
* Shifting to the right by one place is like performing floor(round up decimals) division by 2.

* Examples:

```
a = 1010 
a >> 1 = 101 #the right most bit is eliminated
a >> 2 = 10
a >> 4 = 0
```

```python
a = 10 
print(f"a >> 1: {a >> 1}")
```
```
a >> 1: 5
```
```python
a = 10 
print(f"a >> 4: {a >> 4}")
```
```
a >> 4: 0
```
### Examples of Solving Ordinary Arthimetic Problems with Bit Manipulation

#### 1. Swap Two Numbers Without Using Any additional Variable

```python
# Swap two numbers without using any additional variable or any arthmetic operator

def swap_numbers(a, b):
    """
    Given two integers a and b, swap them without using any additional variable
    Solution: Use bitwise operator XOR(^)
    """
    
    a = a ^ b 
    b = a ^ b # b = a ^ b = (a^b) ^ b = a^(b^b) = a^0 = a, now b = a
    a = a ^ b # a = a ^ b = (a^b) ^ a = b^(a^a) = b ^0 = b, now a = b, swapped!!
    
    return a, b
```
```python
a = 12
b = 32

a_new, b_new = swap_numbers(a,b)
print(f"Swapped A:{a_new}, Swapped B: {b_new}")
```
```
Swapped A:32, Swapped B: 12
```


```python
# Swapping numbers using arthmetic operators

def swap_numbers_2(a, b):
    """
    Given two integers a and b, swap them without using any additional variable
    Solution: Use bitwise operator XOR(^)
    """
    
    a = b - a
    b = b - a # b = b - (b - a) = b - b + a = a, b = a, swapped!
    a = b + a # a = b + a = 
    
    return a, b
```
```python
a = 12
b = 32

swap_numbers_2(a, b)
```
```
(32, 12)
```

#### 2. Add Two Numbers Without Using Arthmetic Operations

```python
# Add two numbers without using any arthmetic operator

#1: Using iterative approach

def add_without_arthimetic_iter(a, b):
    """
    Given 2 numbers, return their sum without using arthmetic operator.

    Solution: 
        Step 1: Add two numbers without carrying the carry. This is peformed by XOR in binary.
        Step 2: Add them together but only carry (ith bit in carry bits is 1 if ith-1 of a and b are 1 (1 + 1 = 10, sum = 0, carry = 1)
        Do those 2 steps iteratively.
    """

    
    
    if b == 0:
        return a
    
    while b != 0:
        sum_no_carry = a ^ b
        carry = (a & b) << 1
        
        a = sum_no_carry
        b = carry
    
    return a
```
```python
a = 12
b = 13

add_without_arthimetic_iter(a, b)
```
```
25
```

```python
#2: Add two numbers iteratively

def add_without_arthimetic_recursive(a, b):
    """
      Given 2 numbers, return their sum without using arthmetic operator.

    Solution: 
        Step 1: Add two numbers without carrying the carry. This is peformed by XOR in binary.
        Step 2: Add them together but only carry (ith bit in carry bits is 1 if ith-1 of a and b are 1 (1 + 1 = 10, sum = 0, carry = 1)
        Do those 2 steps recursively.
    """
    
    if b == 0:
        return a
    
    sum_no_carry = a ^ b
    carry = (a & b) << 1
    
    
    return add_without_arthimetic_recursive(sum_no_carry, carry)
```
```python
a = 12
b = 13

add_without_arthimetic_recursive(a, b)
```
```
25
```


### Further Learning

This is fairly short given the depth of bit manipulation. For more about it, check:

* [Bit Hacks, MIT OpenCourseWare, MIT 6.172](https://www.youtube.com/watch?v=ZusiKXcz_ac)
* [Bitwise Operators in Python by Real Python](https://realpython.com/python-bitwise-operators/#bitwise-logical-operators)
* [Bit Manipulation: Python Official](https://wiki.python.org/moin/BitManipulation)


### To do:

* Revisit bitwise operators and the foundations of binary system to understand this thing more.