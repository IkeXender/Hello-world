hourlyWage = float(input("Enter hourly wage: "))

regularHours = float(input("Enter regular hours: "))

overtimeHours = float(input("Enter overtime hours: "))

regularPay = hourlyWage * regularHours
overtimePay = overtimeHours * (1.5 * hourlyWage)
totalPay = regularPay + overtimePay
print("The total weekly pay is $", round(totalPay, 2))


