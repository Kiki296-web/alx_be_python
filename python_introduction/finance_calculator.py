# User to input monthly income and expenses
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate annual savings with 5% annual interest
annual_savings = monthly_savings * 12
projected_savings = int(annual_savings * 1.05)

# Print output
print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)