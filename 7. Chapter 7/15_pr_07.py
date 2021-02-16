n = 6
for i in range(n): 
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))

for i in range(0,6,1): 
    print(" " * (6-i-1), end=" ")
    print("*" * (2*i+1), end=" ")
    print(" " * (6-i-1))