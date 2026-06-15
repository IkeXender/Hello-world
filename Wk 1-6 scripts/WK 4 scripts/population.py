startPopulation = int(input("Enter the starting population: "))

growthRate = float(input("Enter the growth rate: "))

hoursPerGrowth = float(input("Enter the hours to achieve growth rate: "))

totalHours = float(input("Enter the total hours of growth: "))

cycles = totalHours / hoursPerGrowth

population = startPopulation * (growthRate ** cycles)

print("The predicted population is:", int(population))
