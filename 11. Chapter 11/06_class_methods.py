class Employee:
    company = "Camel"
    salary = 100  #this is class attribute and not a instance attribute which can be changed using
                    # @classmethod or Employee.salary
    location = "Delhi"

    #another way to change class attribute
    # def changeSalary(self, sal):
    #     self.__class__.salary = sal    

    @classmethod
    def changeSalary(cls, sal):  #Note:here self is not passed, cls is passed
        cls.salary = sal

e = Employee()
print(Employee.salary)
print(e.salary)
e.changeSalary(455) #Value at class level changed since method has @classmethod annotation.without 
                        #that instance attribute will be changed
print(e.salary)
print(Employee.salary) #without @classmethod annotation ,value will be 100
