class MyNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num

n1 = MyNumber(4)
n2 = MyNumber(6)
sum = n1 + n2 #without __add__ n1 and n2 will be not added.because it does not understand n1 or n2 which is MyNumber and not a number
mul = n1 * n2
#div = n1 / n2 # __truediv__ should be overloaded else it will give error
print(sum)
print(mul)

