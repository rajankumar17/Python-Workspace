myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1, 2, 5], #list
    "anotherdict": {'harry': 'Player'} # this key has dict has value
}
myDict.update({"newKey":"newValue"})
print(myDict)
print(myDict.items())
print(myDict.keys())
print(myDict.values())
print(myDict['Fast'])
print(myDict['Harry'])
myDict['Marks'] = [45, 78] # Re-assign the value to the dict for key Marks
print(myDict['Marks'])
print(myDict['anotherdict'])
print(myDict['anotherdict']['harry']) # Getting value of the dict inside the dict