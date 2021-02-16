class Employee:
    company = "Google"
    salary = 5000
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")
    
    @staticmethod
    def getGlobalSalary():
        print(f"Static :Salary for this employee working in {Employee.company} is {Employee.salary}")


harry = Employee()
harry.salary = 100000
harry.getSalary() # Employee.getSalary(harry)
Employee.getSalary(harry)
Employee.getGlobalSalary()