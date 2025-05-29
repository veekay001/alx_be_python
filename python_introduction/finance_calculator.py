monthly_income = int(input("Enter your monthly income: "))
total_expenses = int(input("Enter your total monthly expenses: "))

monthy_savings = monthly_income - total_expenses

projected_savings = monthy_savings * 12 + (monthy_savings * 12 * 0.05)

print (f"Your monthly savings are ${monthy_savings}.")
print (f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")