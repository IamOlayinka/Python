accounts = []

class Account:
    def __init__(self, account_id, name, account_type, balance):
        self.account_id = account_id
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "name": self.name,
            "account_type": self.account_type,
            "balance": self.balance
        }

    @staticmethod
    def from_dict(data: dict):
        return Account(
            account_id=str(data.get("account_id")),
            name=data.get("name", ""),
            account_type=data.get("account_type", ""),
            balance=float(data.get("balance", 0.0))
        )

    def __str__(self):
        return f"Account({self.account_id}, {self.name}, {self.account_type}, {self.balance})"
