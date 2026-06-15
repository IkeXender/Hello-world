grossIncome = float(input("Enter the gross income: "))

dependents = int(input("Enter the number of dependents: "))

taxableIncome = grossIncome - (10000 + dependents * 3000)
incomeTax = taxableIncome * 0.20
print("The income tax is $", round(incomeTax, 2))
