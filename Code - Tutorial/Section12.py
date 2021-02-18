listOfAges=[5 , 6, 24, 32, 21, 70]
counter=0
while listOfAges[counter]<30:
    print(counter)
    counter=counter+1

print("Loop stopped for age="+str(listOfAges[counter]))
print("")

counter=0
while listOfAges[counter]<30:
    print(counter)
    if listOfAges[counter]>20:
        print("The value which stopped the outer loop="+str(listOfAges[counter]))
        break
    counter=counter+1

print("")
counter=0
while listOfAges[counter]<70:
    print("Cell's new value is="+str(listOfAges[counter]+2))
    counter=counter+1
else:
    print("I’m inside ‘else’ because of "+str(listOfAges[counter]))