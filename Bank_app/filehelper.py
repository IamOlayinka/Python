from threading import Lock
import os
import json
from bankaccount import Account
from flask import abort


DATA_FILE = 'accounts.json'
file_lock = Lock() # To ensure thread-safe file operations

accounts = {}

def load_accounts_from_file()->dict:
    """Load accounts from the JSON file."""

    if not os.path.exists(DATA_FILE):
        return {} 
     
    with file_lock:
        with open(DATA_FILE, 'r', encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}
    for item in data:
        account = Account.from_dict(item)
        accounts[account.account_id] = account
    return accounts


def save_accounts_to_file(accounts:dict):
    """Save accounts to the JSON file."""
    with file_lock:
        with open(DATA_FILE, 'w', encoding="utf-8") as file:
            data = [account.to_dict() for account in accounts.values()]
            json.dump(data, file, indent=4)        


def get_account_or_404(account_id: str) -> Account:
    acc = accounts.get(str(account_id))
    if not acc:
        abort(404, description="Account not found")
    return acc