from flask import render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe


# Display new recipe Page
@app.route('/recipes/new')
def new_recipes():
    if not "user_id" in session:
        return redirect('/')
    user = User.get_by_id({'id': session["user_id"]})
    return render_template('recipe_new.html', user=user)


# Adds new recipe to DB
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


# Deletes recipe
@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    if not "user_id" in session:
        return redirect('/')
    data = {
            'id': id
    }
    to_be_deleted = Recipe.get_by_id(data)
    if not session['user_id'] == to_be_deleted.user_id:
        flash("Quit trying to delete someone else's recipe")
        return redirect('/')
    Recipe.delete_recipe(data)
    return redirect('/welcome')


# Display one recipe
@app.route('/recipes/<int:id>')
def show_recipe(id):
    if not "user_id" in session:
        return redirect('/')
    data = {
        'id': id
    }
    recipe = Recipe.get_by_id(data)
    user = User.get_by_id({'id': session["user_id"]})
    return render_template("recipe_one.html", recipe=recipe, user=user)


# Edit recipe
@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if not "user_id" in session:
        return redirect('/')
    data = {
            'id': id
    }
    recipe = Recipe.get_by_id(data)
    return render_template("recipe_edit.html", recipe=recipe)


# Update Recipe
@app.route('/recipes/<int:id>/update', methods=["POST"])
def update_recipes(id):
    if not "user_id" in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect(f'/recipes/{id}/edit')
    data = {
        **request.form,
        'id': id
    }
    Recipe.update(data)
    return redirect('/welcome')