class buildings:

    def __init__(self,season_in_year, apartment_number, apartment_size):
        self.season_in_year = season_in_year
        self.apartment_number = int(apartment_number)
        self.apartment_size = int(apartment_size)

    def rent_calculator(self):
        base_price_per_month = 2000
        season_price_buffer = 0
        if self.season_in_year == "summer":
            season_price_buffer = 1.5
        elif self.season_in_year == "winter":
            season_price_buffer = 1.1
        elif self.season_in_year == "spring":
            season_price_buffer = 1.6
        else:
            season_price_buffer = 1.3

        if self.apartment_size > 130:
            season_price_buffer += 0.1
        print("Buffer is : " +str(season_price_buffer))
        total_rent = base_price_per_month * season_price_buffer
        # print("Total rent in the " +self.season_in_year +" is : " +str(total_rent))
        print("Total rent for %s apartment number %s. Apartment's size is : %s meters" %(total_rent,self.apartment_number, self.apartment_size))
        return total_rent


    def monthly_maintenance_pay(self,total_rent):
        manitenance = 0
        if total_rent > 2500:
            manitenance = 100
        else:
            manitenance = 50
        print("Maintenance is %s" %(str(manitenance)))
        print("Maintenance is "+ str(manitenance))



lease_contract_1 = buildings("summer", "4", "135")
total_rent = lease_contract_1.rent_calculator()

lease_contract_1.monthly_maintenance_pay(total_rent)

print("\n")

lease_contract_2 = buildings("winter", "5", "135")
total_rent = lease_contract_2.rent_calculator()

lease_contract_2.monthly_maintenance_pay(total_rent)


