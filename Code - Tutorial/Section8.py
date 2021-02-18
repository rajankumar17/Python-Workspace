set_drinks={"Cola","Sprite","Water","Beer","Soda"}
print(set_drinks)

set_drinks.add("Soda")
set_drinks.add("Fruti")
print(set_drinks)

set_drinks.discard("Soda")
set_drinks.remove("Water")
print(set_drinks)

drinks_2=set_drinks.copy()
print(drinks_2)

print(len(drinks_2))

set_drinks.update("Cherry")