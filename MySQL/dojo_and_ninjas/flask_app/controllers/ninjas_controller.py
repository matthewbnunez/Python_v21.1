from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


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
