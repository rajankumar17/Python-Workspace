employeesDict = {"Jack": 6,"Russel": 10,"Keren": 2}
emplList5To8 = []
emplList2To4 = []
if(employeesDict.get("Jack") >= 5 and employeesDict.get("Jack") <= 8):
    emplList5To8.append("Jack")
elif(employeesDict.get("Russel") >= 5 and employeesDict.get("Russel") <= 8):
    emplList5To8.append("Russel")
elif(employeesDict.get("Keren") >= 5 and employeesDict.get("Keren") <= 8):
    emplList5To8.append("Keren")
else:
    print("No one fits the job")

if(employeesDict.get("Jack") >= 2 and employeesDict.get("Jack") <= 4):
    emplList2To4.append("Jack")
elif(employeesDict.get("Russel") >= 2 and employeesDict.get("Russel") <= 4):
    emplList2To4.append("Russel")
elif(employeesDict.get("Keren") >= 2 and employeesDict.get("Keren") <= 4):
    emplList2To4.append("Keren")
    if(employeesDict["Keren"] == 2):
        pass
    elif(employeesDict["Keren"] == 3):
        pass
    elif(employeesDict["Keren"] == 4):
        pass
    else:
        print('default exit point - nested if')
else:
    print("No one fits the job")
print("Employees having 5 to 8 hrs ="+str(emplList5To8))
print("Employees having 2 to 4 hrs ="+str(emplList2To4))