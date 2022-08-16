from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30min = data['under_30min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    
    # Creates a new Recipe
    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_cooked, under_30min, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30min)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)


    # Update recipe edit
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_cooked = %(date_cooked)s, under_30min = %(under_30min)s"
        return connectToMySQL(DATABASE).query_db(query, data)


    # Getting recipe by id
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes JOIN users on users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        this_recipe = cls(row)
        user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
        }
        chef = user_model.User(user_data)
        this_recipe.chef = chef 
        return this_recipe


    # Display all Recipes
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes Join users on users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_recipes = []
            for row in results:
                this_recipe = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                this_recipe.chef = this_user
                all_recipes.append(this_recipe)
            return all_recipes
        return results


    # Delete a recipe
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


    # Validate
    @staticmethod
    def validator(form_data):
        is_vaild = True
        if len(form_data['name']) < 1:
            flash("Name required")
            is_vaild = False
        if len(form_data['date_cooked']) < 1:
            flash("Date cooked/made required")
            is_vaild = False
        if 'under_30min' not in form_data:
            flash("Under 30 minutes required")
            is_vaild = False
        return is_vaild