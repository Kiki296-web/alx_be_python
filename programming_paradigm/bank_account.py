class BankAccount:

    def __init__(self, account_balance=0):
        self.account_balance = account_balance


    def deposit(self, amount):
        self._account_balance += amount

    def withdraw(self, amount):
        if amount > self._account_balance:
            return False
        else:
            self._account_balance -= amount
            return True

        
    def display_balance(self):
        return f"Current Balance: ${self.account_balance:}"
