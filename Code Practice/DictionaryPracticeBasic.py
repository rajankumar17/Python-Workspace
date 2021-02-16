# Collections - Dictrionary practice (basic)

# Create a dictionary about Alex
alex = {"Age": 32 , "Married" : "Yes", "Kids": 3}
print("(1) - This is Alex's dictionary : " +str(alex))

print(alex['Age'])

# Extract values of the dictionary into variables
age = alex['Age']
marriage_status = alex['Married']
number_of_kids = alex['Kids']

print("(2) - Print of 'age' value : " +str(age))
print("(2) - Print of 'marriage_status' value : " +marriage_status)
print("(2) - Print of 'number_of_kids' value : " +str(number_of_kids))

# Change of 'Age' key cell value from 32 to 33
age_helper_dictionary = {'Age' : 33}
alex.update(age_helper_dictionary)
print("(4) - Alex's age update to '33' : " +str(alex))


kids_helper_dictionary = {'Kids' : 4}
alex.update(kids_helper_dictionary)

# Change of 'Kids' key cell value from 3 to 4
print("(5) - Alex's 'Kids' number update to '4' : " +str(alex))

# Print all keys out of 'alex' dictionary
print("(6) - 'keys' of the dictionary : " +str(alex.keys()))

# Print all 'values' out of 'alex' dictionary
print("(7) - 'values' of the dictionary : " +str(alex.values()))

joe = {'Age' : 35 , 'Kids' : {'David' : 'Boy' , 'Lisa' : 'Girl'}}
print(joe)
