class BankAccount:

    def __init__(self, account_balance):
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance += amount


    def withdraw(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0:
            raise ValueError("Insufficient funds for withdrawal")
        else:
            return self.account_balance
        
    def display_balance(self):
        return f"Current balance: ${self.account_balance:.2f}"
       
        
   