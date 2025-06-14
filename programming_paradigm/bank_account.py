class BankAccount:

    def __init__(self, account_balance=0):
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance += amount


    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
        else:
            self.account_balance -= amount
            print(f"Withdrew ${amount:.2f}")
        
    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"
       
        
   