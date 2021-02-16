gross_salary = 10000
health_insurance = 430.99
rent = 1200
food = 400.5
salary_tax_percent = 0.2
donation_percent = 0.1

tax_deduction_amt = gross_salary*salary_tax_percent
net_sal =  gross_salary-health_insurance-rent-food-tax_deduction_amt
print(str(net_sal))

donation_given = net_sal*donation_percent
print(str(donation_given))


print(str(donation_given.__round__(2)))