import json
import os

# ==============================
# BankAccount Class
# ==============================
class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False
        if amount > self.__balance:
            print("Insufficient funds.")
            return False
        self.__balance -= amount
        return True

    def get_balance(self):
        return self.__balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "owner_name": self.owner_name,
            "balance": self.__balance
        }

    @staticmethod
    def from_dict(data):
        return BankAccount(
            data["account_number"],
            data["owner_name"],
            data["balance"]
        )

    def __str__(self):
        return f"Account {self.account_number} - {self.owner_name}: Balance = {self.__balance}"


# ==============================
# Bank System (handles storage)
# ==============================
class BankSystem:
    FILE_NAME = "accounts.json"

    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as f:
                data = json.load(f)
                for acc_data in data:
                    acc = BankAccount.from_dict(acc_data)
                    self.accounts[acc.account_number] = acc
        else:
            self.accounts = {}

    def save_accounts(self):
        data = [acc.to_dict() for acc in self.accounts.values()]
        with open(self.FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)

    def create_account(self, account_number, owner_name, balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
            return
        acc = BankAccount(account_number, owner_name, balance)
        self.accounts[account_number] = acc
        self.save_accounts()
        print("✅ Account created successfully!")

    def get_account(self, account_number):
        return self.accounts.get(account_number)


# ==============================
# Main Menu
# ==============================
bank = BankSystem()

print("Welcome to Python Bank!")

while True:
    print("\n1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    try:
        choice = int(input("Choose option (1-5): ").strip())
    except ValueError:
        print("Invalid input. Enter a number.")
        continue

    if choice == 1:
        acc_num = input("Enter account number: ").strip()
        name = input("Enter owner name: ").strip()
        try:
            bal = float(input("Enter initial balance: ").strip())
        except ValueError:
            bal = 0
        bank.create_account(acc_num, name, bal)

    elif choice == 2:
        acc_num = input("Enter account number: ").strip()
        acc = bank.get_account(acc_num)
        if acc:
            try:
                amt = float(input("Deposit amount: ").strip())
            except ValueError:
                print("Invalid amount.")
                continue
            if acc.deposit(amt):
                bank.save_accounts()
                print("✅ Deposit successful!")
        else:
            print("❌ Account not found.")

    elif choice == 3:
        acc_num = input("Enter account number: ").strip()
        acc = bank.get_account(acc_num)
        if acc:
            try:
                amt = float(input("Withdraw amount: ").strip())
            except ValueError:
                print("Invalid amount.")
                continue
            if acc.withdraw(amt):
                bank.save_accounts()
                print("✅ Withdrawal successful!")
        else:
            print("❌ Account not found.")

    elif choice == 4:
        acc_num = input("Enter account number: ").strip()
        acc = bank.get_account(acc_num)
        if acc:
            print(f"💰 Balance: {acc.get_balance()}")
        else:
            print("❌ Account not found.")

    elif choice == 5:
        bank.save_accounts()
        print("✅ All accounts saved. Goodbye!")
        break

    else:
        print("Invalid option.")
