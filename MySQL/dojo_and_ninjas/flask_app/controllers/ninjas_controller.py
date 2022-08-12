from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


# DISPLAYS ALL Ninja
@app.route("/ninjas")
def read_all():
    ninjas = Ninja.get_all()
    print(ninjas)
    return render_template("Dojo_Show.html", all_ninjas=ninjas)


# CREATES A NEW Ninja
@app.route("/ninjas/new")
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template("create.html", all_dojos = all_dojos)


# SAVES NEW Ninja IN DB
@app.route('/ninjas/create', methods=["POST"])
def createN():
    Ninja.create_ninja(request.form)
    return redirect('/')
