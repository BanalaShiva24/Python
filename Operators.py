#Arithmetic Operators
num1 = 10
num2 = 3
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
print("Sum:", sum)
print("Difference:", difference)   
print("Product:", product)
print("Quotient:", quotient)
print("Modulus:", num1 % num2)  # Remainder
print("Exponentiation:", num1 ** num2)  # num1 raised to the power of num2
print("Floor Division:", num1 // num2)  # Quotient without the decimal part
#Relational Operators
a = 5
b = 10    
print(a > b)   # False
print(a < b)   # True    
print(a == b)  # False
print(a != b)  # True
print(a >= b)  # False
print(a <= b)  # True
#Logical Operators
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
print(not y)    # True
#Assignment Operators
c = 5
c += 3  # c = c + 3
c -= 2  # c = c - 2
c *= 4  # c = c * 4
c /= 2  # c = c / 2
print(c)
#Bitwise Operators
p = 5  # 0101 in binary
q = 3  # 0011 in binary
print(p & q)  # Bitwise AND: 0001 (1 in decimal)
print(p | q)  # Bitwise OR: 0111 (7 in decimal)
print(p ^ q)  # Bitwise XOR: 0110 (6 in decimal)
print(~p)     # Bitwise NOT: -0110 (-6 in decimal)
print(p << 1) # Left Shift: 1010 (10 in decimal)
print(p >> 1) # Right Shift: 0010 (2 in decimal)  
#Membership Operators
list1 = [1, 2, 3, 4, 5]
print(3 in list1)   # True
print(6 not in list1) # True
print(2 in list1)   # True
print(7 not in list1) # True
#Identity Operators
m = 10
n = 10
print(m is n)   # True
print(m is not n) # False
n = 20
print(m is n)   # False
print(m is not n) # True