from flask import Flask,render_template,jsonify,request,redirect,url_for,abort
from bankaccount import Account
from filehelper import load_accounts_from_file, save_accounts_to_file, get_account_or_404

app = Flask(__name__)   

accounts = load_accounts_from_file()
      
@app.route('/bank', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/account_detail', methods=['POST'])
def account_detail():
    account_id = request.form.get('account_id')
    acc = get_account_or_404(account_id)
    account = jsonify(acc.to_dict())
    return render_template("account_detail.html", account=account)

@app.route('/accounts' , methods=['GET'])
def list_accounts():
    account_list = [account.to_dict() for account in accounts.values()]
    return render_template('accounts.html', accounts=account_list)


@app.route("/accounts/<account_id>", methods=["GET"])
def get_account(account_id):
    acc = get_account_or_404(account_id)
    account = acc.to_dict()
    return render_template("account_detail.html", account=account)

@app.route("/accounts/create", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        data = request.form
        account_id = str(data.get("account_id")).strip()
        name = str(data.get("name","")).strip()
        account_type = str(data.get("account_type")).strip()
        balance = float(data.get("balance", 0.0).strip())
        
        if not account_id or not name or not account_type:
            abort(400, description="Missing required fields")
        
        if account_id in accounts:
            abort(400, description="Account ID already exists")

        new_account = Account(account_id, name, account_type, balance)
        accounts[account_id] = new_account
        save_accounts_to_file(accounts)

        return redirect(url_for("list_accounts"))

    return render_template("create_account.html")

@app.route("/accounts/<account_id>/deposit", methods=["GET", "POST"])
def deposit(account_id):
    acc = get_account_or_404(account_id)
    if request.method == "POST":
        amount = float(request.form["amount"])
        try:
            acc.deposit(amount)
            save_accounts_to_file(accounts)
            return redirect(url_for("get_account", account_id=account_id))
        except ValueError as e:
            return str(e), 400
    return render_template("deposit.html", account=acc)  
@app.route("/accounts/<account_id>/withdraw", methods=["GET", "POST"])
def withdraw(account_id):
    acc = get_account_or_404(account_id)
    if request.method == "POST":
        amount = float(request.form["amount"])
        try:
            acc.withdraw(amount)
            save_accounts_to_file(accounts)
            return redirect(url_for("get_account", account_id=account_id))
        except ValueError as e:
            return str(e), 400
    return render_template("withdraw.html", account=acc)    

@app.route("/account/<account_id>/edit", methods=["GET", "POST"])
def edit_account(account_id):  
    print("Editing account:", account_id)         
    if account_id not in accounts:
        return "Account not found", 404

    if request.method == "POST":
        accounts[account_id]["name"] = request.form["name"]
        accounts[account_id]["account_type"] = request.form["account_type"]
        accounts[account_id]["balance"] = int(request.form["balance"])
        print("Updated account:", accounts[account_id])
        return redirect(url_for("list_accounts"))

    return render_template("edit_account.html", account=accounts[account_id], account_id=account_id)    
@app.route("/accounts/<account_id>/delete")
def delete_account(account_id):
    if account_id in accounts:
        del accounts[account_id]
    return redirect(url_for("list_accounts"))   


if __name__ == '__main__':
    app.run(debug=True)