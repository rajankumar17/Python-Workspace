# Curly braces or the set() function can be used to create sets. 
# Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary,
a = {1, 3, 4, 5, 1}
print(type(a))
print(a)  #{1, 3, 4, 5}
# b = set(1, 3, 4, 5, 1) --> error ...at most 1 argument allowed
# b = set(1) --> error ...'int' object is not iterable
b = set('13451')  # String is iterable
print(type(b)) 
print(b) #{'4', '3', '1', '5'} as SET can be in any order.Note :here all values are String in single quote '
c = set()
c.add(1)
c.add(3)
c.add(4)
c.add(5)
c.add(1)
print(type(c))
print(c) #{1, 3, 4, 5}