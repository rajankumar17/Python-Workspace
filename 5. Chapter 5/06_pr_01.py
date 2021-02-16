myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
# Below line will NOT throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))
# Below line will throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict[a])


