class Car:

    def __init__(self,fuel_status,current_km_on_engine,door_status):
        self.fuel_status = fuel_status
        self.current_km_on_engine = current_km_on_engine
        self.door_status = door_status

    def fuel_calculator(self):
        print("You still have "+str(self.fuel_status)+" liters of fuel")

    def check_engine(self):
        print("You need check in "+str(self.current_km_on_engine)+" more kilometers")

    def door_is_open_check(self):
        if self.door_status=="closed":
            print("All doors are "+str(self.door_status))
        else:
            print("Not all doors are closed")

fordCar=Car(10,240,"closed")
fordCar.fuel_calculator()
fordCar.check_engine()
fordCar.door_is_open_check()

audiCar=Car(25,310,"opened")
audiCar.fuel_calculator()
audiCar.check_engine()
audiCar.door_is_open_check()