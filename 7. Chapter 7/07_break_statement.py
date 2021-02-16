for i in range(6):
    print(i)
    if i == 5:
        print("Breaking before end")
        break
else:
    print("This is inside else of for : Loop completed")
print("------------------------------")
for i in range(6):
    print(i)
    if i == 5:
        continue
else:
    print("This is inside else of for : Loop completed")
print("------------------------------")
for i in range(6):
    print(i)
    
else:
    print("This is inside else of for : Loop completed")