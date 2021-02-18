myTuple = ("python", "pycharm IDE", "tuple", "collections", "string")
print(myTuple)
print(type(myTuple))

print("we are ninja developers. We write "+myTuple[0] + " code in "+myTuple[1] +
      " , and now practicing "+myTuple[-3]+" collections topic, that contains "+myTuple[-1]+" variables.")

listOfTuple=list(myTuple)
listOfTuple.append("float")
listOfTuple.append("list")
myTuple=tuple(listOfTuple)

print(listOfTuple)
print(type(listOfTuple))

print(myTuple)
print(type(myTuple))

singleTuple=(1,)
print(singleTuple)
print(type(singleTuple))