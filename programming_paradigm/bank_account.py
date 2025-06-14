class BankAccount:

    def __init__(self, account_balance=0):
        self.account_balance = account_balance


    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self._account_balance += amount
        return f"Deposited ${amount:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self._account_balance:
            return "Insufficient funds."
        self._account_balance -= amount
        return f"Withdrew ${amount:.2f}"

        
    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"
    