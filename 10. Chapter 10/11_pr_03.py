class Sample:
    a = "Harry"

obj = Sample()
obj1 = Sample()
obj.a = "Vikky"
Sample.a = "Rikky" # Value of global variable changed here

print(Sample.a)
print(obj.a)
print(obj1.a)