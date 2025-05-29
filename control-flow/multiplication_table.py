#User to input number for a multiplication table
number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number* i}")