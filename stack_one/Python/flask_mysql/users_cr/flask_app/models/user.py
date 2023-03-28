
from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['fname']) <= 2:
            flash("name must be more than 2 characters")
            is_valid = False
        if len(data['lname']) <= 1:
            flash('last name must be more than 1 character')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_cr').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
        return  connectToMySQL('users_cr').query_db(query, data)

    @classmethod
    def delete_user(cls, user_id_dict):
        query = "DELETE FROM users WHERE id = %(user_id)s;"
        return  connectToMySQL('users_cr').query_db(query, user_id_dict)

    @classmethod
    def edit_user(cls, data):
        query = """UPDATE users
        SET first_name = %(fname)s, 
        last_name = %(lname)s, 
        email = %(email)s 
        WHERE id = %(id)s;"""
        return  connectToMySQL('users_cr').query_db(query, data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        results = connectToMySQL('users_cr').query_db(query, data)
        return cls(results[0])

