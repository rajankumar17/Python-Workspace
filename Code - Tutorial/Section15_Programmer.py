from Section15_Employee import Employee


class Programmer(Employee):

    def __init__(self, years_of_experience, position_name, employee_name):
        super().__init__(years_of_experience, position_name, employee_name)
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name
        


programmer1 = Programmer(3, "Lead", "Rajan")
junior_python_programmer=Programmer(1, "front-end","Joseph")
senior_devops=Programmer(6, "senior_devops", "Dan")

programmer1sal = programmer1.calculate_salary()
programmer1netSal= programmer1sal + programmer1.candidate_for_bonus(programmer1sal)

junior_python_programmersal = junior_python_programmer.calculate_salary()
junior_python_programmernetSal= junior_python_programmersal + junior_python_programmer.candidate_for_bonus(junior_python_programmersal)

senior_devopssal = senior_devops.calculate_salary()
senior_devopsnetSal= senior_devopssal + senior_devops.candidate_for_bonus(senior_devopssal)
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


