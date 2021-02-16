class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6100

    @property  # totalSalary will be treated as property and not a method
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.salary)
print(e.salarybonus)
print(e.totalSalary)  # note here its called as e.totalSalary and not as e.totalSalary()
e.totalSalary = 5800  # when totalSalary is set,the value of salarybonus is also changed
print("---------------") 
print(e.salary)
print(e.salarybonus)
print(e.totalSalary)