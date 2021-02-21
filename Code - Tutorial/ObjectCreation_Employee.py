class Employee:

    def __init__(self, name, salary, attendance):
        self.name = name
        self.salary = salary
        self.attendance = attendance

    def attendance_check(self):
        print("" +self.name +"'s attendance " +"status is : " +str(self.attendance))

    def show_employees_details(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)

sara = Employee("sara", "1000", False)
sara.show_employees_details()
sara.attendance_check()

michael = Employee("michael", "3000" , True)
michael.show_employees_details()
michael.attendance_check()





