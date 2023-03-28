from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user #use user.User to avoid circular imports in your models
from flask import session,flash

db = 'recipes_schema'
class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.date_cooked = data['date_cooked']
        self.chef = None



    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) == 0:
            flash("name must not be blank")
            is_valid = False
        if len(data['description']) == 0:
            flash("description must not be blank")
            is_valid = False
        if len(data['instructions']) == 0:
            flash("instructions must not be blank")
            is_valid = False
        if len(data['date_cooked']) == 0:
            flash("date must not be blank")
            is_valid = False
        if 'under_30' not in data:
            flash("please select yes or no for cooked in under 30 minutes")
            is_valid = False
        return is_valid

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id"
        results = connectToMySQL(db).query_db(query)
        recipes = []
        for each_recipe in results:
            recipe = cls(each_recipe)
            user_data = {
                'id' : each_recipe['users.id'],
                'first_name' : each_recipe['first_name'],
                'last_name' : each_recipe['last_name'],
                'email' : each_recipe['email'],
                'password' : each_recipe['password'],
                'created_at' : each_recipe['users.created_at'],
                'updated_at' : each_recipe['users.updated_at']
                }
            recipe.chef = user.User(user_data)
            recipes.append(recipe)
        return recipes



    @classmethod
    def get_recipe_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(recipe_id)s;"
        results = connectToMySQL(db).query_db(query, data)
        recipe = cls(results[0])
        return recipe



    @classmethod
    def create_recipe(cls, data):
        query =  "INSERT INTO recipes (name, description, instructions, under_30, user_id, date_cooked, created_at, updated_at) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(user_id)s, %(date_cooked)s, NOW(), NOW());"
        return  connectToMySQL(db).query_db(query, data)



    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return  connectToMySQL(db).query_db(query, data)



    @classmethod
    def edit_recipe(cls, data):
        query = """UPDATE recipes
        SET name = %(name)s,
        description = %(description)s,
        instructions = %(instructions)s,
        date_cooked = %(date_cooked)s,
        under_30 = %(under_30)s
        WHERE id = %(id)s;"""
        return  connectToMySQL(db).query_db(query, data)
