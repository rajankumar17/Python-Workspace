# Assignment 3

list = [1, 2, 3, 4]
try:
    print(list[6])
    print("xxx")
except:
    print("Tried to pull index '6' while only '3' are available")
    print(list[8])