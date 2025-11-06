from flask import Flask,render_template,jsonify,request,redirect,url_for

app = Flask(__name__)


users = {
    "1": {"name": "John", "age": 25},
    "2": {"name": "Mary", "age": 30}
}

@app.route('/users', methods=['GET'])
def list_users():
    return render_template('users.html', users=users)


@app.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        user_id = request.form["id"]
        name = request.form["name"]
        age = request.form["age"]

        users[user_id] = {"name": name, "age": int(age)}

        return redirect(url_for("list_users"))

    return render_template("create_user.html")

@app.route("/users/<user_id>/edit", methods=["GET", "POST"])
def edit_user(user_id):
    if user_id not in users:
        return "User not found", 404

    if request.method == "POST":
        users[user_id]["name"] = request.form["name"]
        users[user_id]["age"] = int(request.form["age"])
        return redirect(url_for("list_users"))

    return render_template("edit_user.html", user=users[user_id], user_id=user_id)
@app.route("/users/<user_id>/delete")
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
    return redirect(url_for("list_users"))

if __name__ == '__main__':
    app.run(debug=True)