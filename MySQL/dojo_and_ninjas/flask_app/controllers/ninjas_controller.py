from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja


# DISPLAYS ALL Ninja
@app.route("/")
def read_all():
    ninjas = Ninja.get_all()
    print(ninjas)
    return render_template("read_all.html", all_ninjas=ninjas)


# DISPLAYS ONE NinjaS
@app.route("/ninjas/<int:id>")
def read_one(id):
    data = {
        "id": id
    }
    ninja = Ninja.get_one(data)
    return render_template("read_one.html", ninja=ninja)


# CREATES A NEW Ninja
@app.route("/ninjas/new")
def new_ninja():
    return render_template("create.html")


# SAVES NEW Ninja IN DB
@app.route('/ninjas/create', methods=["POST"])
def create(id):
    Ninja.save(request.form)
    return redirect('/')


# EDIT Ninja
@app.route('/ninjas/<int:id>/edit')
def edit(id):
    data = {
        "id": id
    }
    ninja = Ninja.get_one(data)
    return render_template("edit_user.html", ninja=ninja)


# UPDATE Ninja EDIT IN DB
@app.route('/ninjas/<int:id>/update', methods=["POST"])
def update(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "id": id
    }
    Ninja.update(data)
    return redirect("/")


# DELETE Ninja
@app.route('/ninjas/<int:id>/delete')
def delete(id):
    data = {
        "id": id
    }
    Ninja.delete(data)
    return redirect("/")
