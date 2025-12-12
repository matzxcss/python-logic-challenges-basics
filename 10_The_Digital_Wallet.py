class DigitalWallet:
    def __init__(self, account_name, initial_balance=0):
        self.account_name = account_name
        self.balance = initial_balance
        self.transaction_history = []  # A memória do banco!

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +{amount}")
            print(f"Deposited {amount}. New Balance: {self.balance}")
            return True
        print("Invalid deposit amount.")
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw: -{amount}")
            print(f"Withdrew {amount}. New Balance: {self.balance}")
            return True
        print("Insufficient funds or invalid amount.")
        return False

    def get_statement(self):
        print(f"\n--- Statement for {self.account_name} ---")
        print(f"Current Balance: {self.balance}")
        print("History:")
        for transaction in self.transaction_history:
            print(transaction)
            
# Example usage (pra você testar se funfa):
# my_wallet = DigitalWallet("Matheus Lacerda", 100)
# my_wallet.deposit(50)
# my_wallet.withdraw(30)
# my_wallet.get_statement()
