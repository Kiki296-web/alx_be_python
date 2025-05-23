#User to put the monthly income:
monthly_income = int(input("Enter your monthly income"))
total_month_expenses = int(input("Enter your total monthly expenses"))

#Calculating Monthly savings 
monthly_savings = monthly_income - total_month_expenses

#Calculate annual savings with annual ineterest of 5%

projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

#Printing output

print("Your monthly saving are $",monthly_savings)
print("Projected savings after one year, with interest, is: $",projected_savings)
