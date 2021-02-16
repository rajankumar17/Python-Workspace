list_of_cars = ["BMW","TOYOTA","TESLA","KIA"]
print(list_of_cars)
print(len(list_of_cars))

print(list_of_cars[len(list_of_cars)-2])
print(list_of_cars[-2])

print("TOYOTA"==list_of_cars[1])

list_of_mixed_values=["Jim",3500,"Alex",2.53,True]
print(list_of_mixed_values)
print(list_of_mixed_values[0:4])
# print(list_of_mixed_values[6])
list_of_mixed_values.append("Alpha Romeo")
print(list_of_mixed_values)

list_of_employees=["Adam","John","Greg","Diana","Ashley"]

print(list_of_employees)
print(len(list_of_employees))

list_of_employees[1]="Jack"
print(list_of_employees)

list_of_employees.insert(3,"Mavnik")
print(list_of_employees)

list_of_employees.remove("Mavnik")
list_of_employees.append("Mavnik")
print(list_of_employees)

list_of_employees.pop()
print(list_of_employees)

list_of_employees.sort()
print(list_of_employees)