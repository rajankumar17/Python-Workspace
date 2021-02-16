a = 3
b = 4
c,d=5,6
print(a,b,c,d)
print(-a,-b,-c,-d) #negate
# Arithmetic Operators
print("The value of 3+4 is ", 3+4)
print("The value of 3-4 is ", 3-4)
print("The value of 3*4 is ", 3*4)
print("The value of 3/4 is ", 3/4)
print("The value of 3**4 is ", 3**4) #power
print("The value of 3**4 is ", pow(3,4)) #power
# Assignment Operators
a = 34
print(a)
a -= 12
print(a)
a *= 12
print(a)
a /= 12
print(a)

# Comparison Operators
b = (14<=7)
print(b)
b = (14>=7)
print(b)
b = (14<7)
print(b)
b = (14>7)
print(b)
b = (14==7)
print(b)
b = (14!=7)
print(b)

# Logical Operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))

#Number system
print(bin(25))
print(hex(25))
print(oct(25))
print(0b11001)
print(0x19)
print(0o31)