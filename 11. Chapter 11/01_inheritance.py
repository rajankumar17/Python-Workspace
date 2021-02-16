class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

    def showInheritedDetails(self):
        print("This is an inherited method")

class Programmer(Employee):
    language = "Python"
    # company = "Youtube"

    def getLanguage(self):
        #return self.language
        print(f"The language is {self.language}")
    
    def showDetails(self):
        print("This is an programmer")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
p.getLanguage()
print(p.company) #inherited attribute
p.showInheritedDetails()