from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


db = 'python_exam_schema'


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sightings = []

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
        
    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['fname']) <= 2:
            flash("name must be more than 2 characters")
            is_valid = False
        if len(data['lname']) <= 2:
            flash('last name must be more than 1 character')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash('passwords need to match')
        if  len(data['password']) < 8 or len(data['confirm_password']) < 8:
            flash('please create a password with more than 6 characters')
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(hashed_password)s, NOW(), NOW());"
        return  connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE users.email = %(email)s"
        result = connectToMySQL(db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE users.id = %(user_id)s"
        result = connectToMySQL(db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
