# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n
n=input("enter the number=")
def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

def summation(n):
    if n==0:
        return 0
    return summation(n-1) +n

print(f"Factorial of {n}={factorial(int(n))}")
print(f"sum of all number till {n}={summation(int(n))}")