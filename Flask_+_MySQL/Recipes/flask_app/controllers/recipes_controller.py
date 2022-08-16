from flask import render_template, redirect, request, flash, session
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe


@app.route('/recipes/new')
def new_recipes():
    if not "user_id" in session:
        return redirect('/')
    user = User.get_by_id({'id': session["user_id"]})
    return render_template('recipe_new.html', user=user)


@app.route('/recipes/create', methods=["POST"])
def create_recipes():
    if not "user_id" in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        'user_id': session["user_id"]
    }
    Recipe.create_recipe(data)
    return redirect('/welcome')