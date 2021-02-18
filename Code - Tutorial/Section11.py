businesses_list = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 10, 15001]
totalTax=0
for income in businesses_list:
    tax=0
    if(income >=1000 and income<=2000):
        tax=0.05*income
    elif(income >2000 and income<=5000):
        tax=0.10*income
    elif(income >5000 and income<=15000):
        tax=0.15*income
    elif(income >15000):
        tax=0.17*income
    else:
        pass
    totalTax=totalTax+tax
    # healthCare = 0.02*(income - tax)
    netIncome=income - tax
    netIncomeAfterHealthCare = netIncome * 0.98
    incomeVsTaxDict ={income:netIncomeAfterHealthCare}
    print(incomeVsTaxDict)
else:
    print("total tax="+str(totalTax))
    print("Done")


fruits="BANANA"
for each_char in fruits:
    print(each_char,end="")

# vscode://vscode.github-authentication/did-authenticate?windowid=1&code=53e78e499dfa25129b1a&state=de7b2541-0643-492d-a8db-22e712a99db9