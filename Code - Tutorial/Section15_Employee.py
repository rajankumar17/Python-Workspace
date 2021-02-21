class Employee:

    def __init__(self,years_of_experience,position_name,employee_name):
        self.years_of_experience=years_of_experience
        self.position_name=position_name
        self.employee_name=employee_name


    def calculate_salary(self):
        if self.years_of_experience <=2:
            salary_raised=1500
        elif self.years_of_experience>2 and self.years_of_experience<=5:
            salary_raised=2500
        else:
            salary_raised=3500

        return salary_raised

    def candidate_for_bonus(self,calculated_sal):
        bonus=0
        if self.position_name=="front_end":
            bonus=0.1*calculated_sal
            if self.years_of_experience>2:
                bonus=0.2*calculated_sal+bonus
        elif self.years_of_experience>2:
            bonus=0.2*calculated_sal
        return bonus

class Programmer(Employee):

    def __init__(self, years_of_experience, position_name, employee_name):
        super().__init__(years_of_experience, position_name, employee_name)
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name



emp1 = Employee(2,"front_end","ankur")
programmer1 = Programmer(3, "Lead", "Rajan")
junior_python_programmer=Programmer(1, "front-end","Joseph")
senior_devops=Programmer(6, "senior_devops", "Dan")

emp1sal = emp1.calculate_salary()
emp1salnetSal= emp1sal + emp1.candidate_for_bonus(emp1sal)

programmer1sal = programmer1.calculate_salary()
programmer1netSal= programmer1sal + programmer1.candidate_for_bonus(programmer1sal)

junior_python_programmersal = junior_python_programmer.calculate_salary()
junior_python_programmernetSal= junior_python_programmersal + junior_python_programmer.candidate_for_bonus(junior_python_programmersal)

senior_devopssal = senior_devops.calculate_salary()
senior_devopsnetSal= senior_devopssal + senior_devops.candidate_for_bonus(senior_devopssal)

# print("Salary is incremented by amount ="+str(emp1.calculate_salary()))
# print("bonus received ="+str(emp1.candidate_for_bonus(emp1.calculate_salary())))

print("Programmer Details - Name ="+str(emp1.employee_name) +
      ", Position ="+str(emp1.position_name)
      +",Years of exp ="+str(emp1.years_of_experience)
      +", Salary ="+str(emp1salnetSal))

print("Programmer Details - Name ="+str(programmer1.employee_name) +
      ", Position ="+str(programmer1.position_name)
      +",Years of exp ="+str(programmer1.years_of_experience)
      +", Salary ="+str(programmer1netSal))

print("Programmer Details - Name ="+str(junior_python_programmer.employee_name) +
      ", Position ="+str(junior_python_programmer.position_name) +
      ",Years of exp="+str(junior_python_programmer.years_of_experience)+
      ",Salary="+str(junior_python_programmernetSal))

print("Programmer Details - Name ="+str(senior_devops.employee_name) +
      ", Position ="+str(senior_devops.position_name)
      +", Years of exp ="+str(senior_devops.years_of_experience)
      +", Salary ="+str(senior_devopsnetSal))


