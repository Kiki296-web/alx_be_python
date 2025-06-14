class BankAccount:

    def __init__(self, account_balance=0):
        self.account_balance = account_balance


    def deposit(self, amount):
        self._account_balance += amount
        return f"Deposited: ${amount:}"

    def withdraw(self, amount):
        if amount > self._account_balance:
            return "Insufficient funds."
        else:
            self._account_balance -= amount
            return f"Withdrew: ${amount:}"

        
    def display_balance(self):
        return f"Current Balance: ${self.account_balance:}"
    