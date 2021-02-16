class Person:
    state = "Las Vegas"
    country = "India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"
    state = "New York"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"
    
    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreath(self):
        print("I am a Progarmmer so I am breathing++..")

p = Person()
p.takeBreath()
# print(p.company) # throws an error

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)
print(pr.state) #inherited from the nearest classs inherited
