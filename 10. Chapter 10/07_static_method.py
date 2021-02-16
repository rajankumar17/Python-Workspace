class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!") # Employee.getSalary(harry)
Employee.greet()
Employee.time()
# if annotation @staticmethod is removed form the method,below call won't work 
# for them to work the second option is the method should have self as parameter
harry.greet() # Employee.greet()
harry.time()

