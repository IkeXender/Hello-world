starting_salary = float(input("Enter the starting salary: "))
increase_percent = float(input("Enter the annual percentage increase: "))
years = int(input("Enter the number of years: "))

salary = starting_salary

print()
print("Year\tSalary")
print("--------------------")

for year in range(1, years + 1):
    print(year, "\t${:,.2f}".format(salary))
    salary = salary * (1 + increase_percent / 100)
