purchase_price = float(input("Enter the purchase price: $"))

down_payment = purchase_price * 0.10
balance = purchase_price - down_payment

annual_rate = 0.12
monthly_payment = purchase_price * 0.05

print("\nDown Payment: ${:.2f}".format(down_payment))
print("Monthly Payment: ${:.2f}".format(monthly_payment))

print()
print("Month\tBalance\t\tInterest\tPrincipal\tPayment\t\tRemaining")
print("----------------------------------------------------------------------")

month = 1

while balance > 0:

    interest = balance * annual_rate / 12

    payment = monthly_payment

    if payment > balance + interest:
        payment = balance + interest

    principal = payment - interest

    remaining_balance = balance - principal

    print(
        "{}\t${:.2f}\t\t${:.2f}\t\t${:.2f}\t\t${:.2f}\t\t${:.2f}".format(
            month,
            balance,
            interest,
            principal,
            payment,
            max(0, remaining_balance)
        )
    )

    balance = remaining_balance
    month += 1
