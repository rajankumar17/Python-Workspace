num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3): 
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")

if(num1>num2 and num1>num3 and num1>num4):
    print(str(num1) + " is greatest")
elif(num2>num1 and num2>num3 and num2>num4):
    print(str(num2) + " is greatest")
elif(num3>num1 and num3>num2 and num3>num4):
    print(str(num3) + " is greatest")
else:
    print(str(num4) + " is greatest")