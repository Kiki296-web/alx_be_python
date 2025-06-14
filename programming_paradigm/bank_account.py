class BankAccount:

    def __init__(self, account_balance=0):
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance += amount


    def withdraw(self, amount):
        if amount > self.account_balance:
            raise ValueError("Insufficient funds.")
        else:
            self.account_balance -= amount
            return self.account_balance
        
    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"
       
        
def main():
    account = BankAccount(100)

    # Test: withdraw more than balance
    try:
        account.withdraw(150)
    except ValueError as e:
        print(e)  # This is what the checker expects

    # Deposit and show balance
    account.deposit(150)
    print(account.display_balance())

if __name__ == "__main__":
    main()