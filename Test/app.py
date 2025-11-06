from flask import Flask,render_template,request
from flask import jsonify

app = Flask(__name__)



accounts = {
    "101": {"name": "Alice"},
    "102": {"name": "Bob"}
}

@app.route('/')
def client():
    return render_template('test_client.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return "This is a simple Flask application."

@app.route("/greet", methods=['POST'])
def greet(): 
    username = request.form['username'] 
    return f"Hello, {username}!"  

@app.route("/search")
def search():
    name = request.args.get('name')
    age = request.args.get('age')
    return f"You searched for: name = {name}, age = {age}"
@app.route("/profile/<username>")
def profile(username):
    return f"Profile page of {username}"

@app.route("/update/<user_id>", methods=['PUT'])
def update_user(user_id):
    if user_id not in accounts:
        return jsonify({"error": "Account not found"}), 404
    
    data = request.get_json()
    accounts[user_id].update(data)
    return jsonify({"message": "Account updated", "account": accounts[user_id]})

@app.route('/delete/<account_id>', methods=['DELETE'])
def delete_account(account_id):
    if account_id in accounts:
        deleted = accounts.pop(account_id)
        return jsonify({"message": "Account deleted", "deleted": deleted})
    else:
        return jsonify({"error": "Account not found"}), 404



@app.route("/api/user")
def api_user():
    return jsonify({"name": "John", "age": 30})


if __name__ == "__main__":
    app.run(debug=True)
