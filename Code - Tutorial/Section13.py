def sorting(*language):
    for lang in language:
        if lang=='Java':
            length =len(lang)
            for i in range(0,length):
                print(lang[i])

sorting('Python','Java')
sorting('Python','Java','Go')
sorting('Python','JS','C++')

def sortings(*language):
    for lang in language:
        if lang=='Java':
            for i in lang:
                print(i)

sortings('Python','Java')
sortings('Python','Java','Go')
sortings('Python','JS','C++')


def tax_calculation(gross_sal,tax=0.22):
    print("In tax calculation with values gross sal= "+str(gross_sal)+" and tax= "+str(tax))
    net_sal=gross_sal-tax
    return net_sal

def salary_limit_tester(net_salary):
    if net_salary>5800:
        return True

net_sal1=tax_calculation(5000,0.2)
net_sal2=tax_calculation(6000,0.22)
net_sal3=tax_calculation(10000)
print("Net sal="+str(net_sal1))
print("Net sal="+str(net_sal2))
print("Net sal="+str(net_sal3))

if salary_limit_tester(net_sal1):
    print(net_sal1)
if salary_limit_tester(net_sal2):
    print(net_sal2)
if salary_limit_tester(net_sal3):
    print(net_sal3)

# Arbitary Keyword Argument
def phone_brands(brand3,brand1,brand2):
    print("The name of brand 3 is ="+str(brand3))

phone_brands(brand1="Armani",brand2="Peter",brand3="Versace")
phone_brands(brand3="Brand3",brand1="Brand 1",brand2="Brand 2")

# Arbitary Keyword Argument
def phone_brands_args(**brand):
    print("The name of brand 3 is ="+str(brand.get("brand3")))
    print("The name of brand 3 is ="+str(brand["brand3"]))

phone_brands_args(brand1="Armani",brand2="Peter",brand3="Versace")
phone_brands_args(brand3="Brand3",brand1="Brand 1",brand2="Brand 2")
