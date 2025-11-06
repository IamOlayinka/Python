from flask import Flask, render_template, request,jsonify


app = Flask(__name__)


users = {
    "1": {"name": "Joshua", "age" : 30, "gender": "Male", "occupation" : " Engineer"},
    "2": {"name": "Emily", "age" : 25, "gender": "Female", "occupation":"Banker"},
    "3" :{"name": "Michael", "age" : 35,"gender": "Male", "occupation" : "Doctor"},
    "4" :{"name": "Sophia", "age" : 28,"gender": "Female", "occupation" : "Artist"}
}

@app.route("/")
def home():
    return "Welcome to the User API!"

@app.route("/users", methods=['GET'])
def get_users():
    return jsonify(users)

@app.route("/createuser")

def create_user_form():
    return render_template('createuser.html')
        
@app.route("/delupdate")
def del_update_form():
    return render_template('user.html')

@app.route("/user/<user_id>")
def get_user(user_id):
    if user_id not in users or user_id is None:
        return jsonify({"error": "User not found"}), 404
    user = users.get(user_id)
    return jsonify(user)

@app.route("/newuser", methods=['POST'])
def create_user():
    name = request.form['name']
    age = request.form['age']   
    gender = request.form['gender']
    occupation = request.form['occupation']
    data = {
        'name': name,
        'age': age,
        'gender': gender,
        'occupation': occupation    
    }
    new_id = str(len(users) + 1)  
    users[new_id] = data
    return jsonify({"message": "User created", "user": users[new_id]}), 201

@app.route('/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        deleted = users.pop(user_id)
        return jsonify({"message": "User deleted", "deleted": deleted})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)