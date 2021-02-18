myDict = {"Age": 32 , "Married" : "Yes", "Kids": 3}
print(myDict)
age=myDict.get("Age")
married=myDict.get("Married")
kids=myDict["Kids"]
print(age)
print(type(age))
print(married)
print(type(married))
print(kids)
print(type(kids))


myDict["Married"]="No"
married=myDict.get("Married")
print(married)
print(myDict)

myKidDict = {"Kids":"5"}
myDict.update(myKidDict)
kids=myDict.get("Kids")
print(kids)
print(myDict)

print(myDict.keys())
print(myDict.values())

building={"floor_first":{"first_apartment":"Rachel","Second_apartment":"Jeen"},"floor_second":{"third_apartment":"Jack"}}
print(building)

floor1=building["floor_first"]
floor2=building["floor_second"]
print(floor1)
print("Person living in 2nd floor="+str(building["floor_second"]["third_apartment"]))
building["floor_second"]["fourth_apartment"]="Carol"
print(building)
building["floor_first"].pop("first_apartment")
print(building)