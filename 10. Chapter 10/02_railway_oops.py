import pandas as pd

class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysApplication = RailwayForm()
harrysApplication.name = "Harry"
harrysApplication.train = "Rajdhani Express"
harrysApplication.printData()
#using pandas dataframe
d1={"Name":[harrysApplication.name],"Train":[harrysApplication.train]}
d=pd.DataFrame(data=d1)
print(d)