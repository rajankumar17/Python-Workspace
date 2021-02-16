class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:
    company = "Visa"
    eCode = 120


class Programmer(Employee,Freelancer): #Order of the inheritance decide which method will be inherited
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.name)
print(p.eCode)
print(p.level)
print(p.company) #Since Employee is inherited first,its company will be called