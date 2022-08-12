from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


# DISPLAYS ALL USERS
@app.route("/")
def read_all():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", all_users=users)


# DISPLAYS ONE USERS
@app.route("/users/<int:id>")
def read_one(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template("read_one.html", user=user)


# CREATES A NEW USER
@app.route("/users/new")
def new_user():
    return render_template("create.html")


# SAVES NEW USER IN DB
@app.route('/users/create', methods=["POST"])
def create():
    User.save(request.form)
    return redirect('/')


# EDIT USER
@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template("edit_user.html", user=user)


# UPDATE USER EDIT IN DB
@app.route('/users/<int:id>/update', methods=["POST"])
def update(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": id
    }
    User.update(data)
    return redirect("/")


# DELETE USER
@app.route('/users/<int:id>/delete')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/")
