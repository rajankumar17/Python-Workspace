greeting = "Good Morning, "
name = "Harry"
print(type(name))

# Concatenating two strings
c = greeting + name
print(c)
print(name[4])
# name[3] = "d" --> Does not work

print(name[1:4])
print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:5]
c = name[-4:-1] # is same is name[1:4]
print(c)

name = "HarryIsGood"
d = name[0::3] # 3rd letter starting from 0 till end
print(d)
d = name[0:6:3] # 3rd letter starting from 0 till 6th letter
print(d)
d = name[0::1] # Start to end incrementing 1 letter
print(d)
d = name[:0:-1] # end to start decrementing 1 letter
print(d)