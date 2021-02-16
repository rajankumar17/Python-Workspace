# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a) # {'a', 'r', 'b', 'c', 'd'}      # unique letters in a
print(a - b)  # letters in a but not in b  {'r', 'd', 'b'}
print(a | b)  # letters in a or b or both {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a.union(b)) # letters in a or b or both {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)  # letters in both a and b {'a', 'c'}
print(a.intersection(b)) # letters in both a and b {'a', 'c'}
print(a ^ b)  # letters in a or b but not both {'r', 'd', 'b', 'm', 'z', 'l'}