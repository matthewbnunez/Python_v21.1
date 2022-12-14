from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo


@app.route("/")
def basic():
    return redirect("/dojo")


# DISPLAYS ALL Ninja
@app.route("/dojos/<int:id>")
def read_all(id):
    data = {
        'id': id
    }
    dojo = Dojo.get_all_ninja(data)
    return render_template("Dojo_Show.html", dojo=dojo)


# DISPLAYS ALL Dojos
@app.route("/dojo")
def read_all_dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("Dojo.html", all_dojos=dojos)


# SAVES NEW Dojo IN DB
@app.route('/dojos/create', methods=["POST"])
def createD():
    Dojo.create_dojo(request.form)
    return redirect('/')