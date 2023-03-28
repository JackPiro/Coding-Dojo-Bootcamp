from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user #use user.User to avoid circular imports in your models
from flask import session,flash

db = 'python_exam_schema'

class Sighting:
    def __init__(self, data):
        self.id = data['id']
        self.what_happened = data['what_happened']
        self.location = data['location']
        self.date_sighted = data['date_sighted']
        self.user_id = data['user_id']
        self.number_of_squatches = data['number_of_squatches']
        self.camper = None



    @staticmethod
    def validate_sighting(data):
        is_valid = True
        if len(data['what_happened']) == 0:
            flash("All fields must be filled out")
            is_valid = False
        if len(data['location']) == 0:
            flash("Location cant be blank")
            is_valid = False
        if len(data['number_of_squatches']) < 1 or None:
            flash("Number of sasquatches must not be zero")
            is_valid = False
        if len(data['date_sighted']) == 0:
            flash("Date sighted must be filled in")
            is_valid = False
        return is_valid



    @classmethod
    def get_all_sightings(cls):
        query = "SELECT * FROM sightings JOIN users ON sightings.user_id = users.id;"
        results = connectToMySQL(db).query_db(query)
        sightings = []
        for each_sighting in results:
            sighting = cls(each_sighting)
            user_data = {
                'id' : each_sighting['users.id'],
                'first_name' : each_sighting['first_name'],
                'last_name' : each_sighting['last_name'],
                'email' : each_sighting['email'],
                'password' : each_sighting['password'],
                'created_at' : each_sighting['users.created_at'],
                'updated_at' : each_sighting['users.updated_at']
                }
            sighting.camper = user.User(user_data)
            sightings.append(sighting)
        return sightings



    @classmethod
    def create_sighting(cls, data):
        query = """INSERT INTO sightings (what_happened, location, date_sighted, number_of_squatches, user_id, created_at, updated_at)
        VALUES (%(what_happened)s, %(location)s, %(date_sighted)s, %(number_of_squatches)s, %(user_id)s, NOW(), NOW());"""
        return connectToMySQL(db).query_db(query, data)



    @classmethod
    def get_sighting_by_id(cls, data):
        query = "SELECT * FROM sightings WHERE id = %(sighting_id)s"
        results = connectToMySQL(db).query_db(query, data)
        sighting = cls(results[0])
        return sighting

    @classmethod
    def delete_sighting(cls, data):
        query = "DELETE FROM sightings WHERE id = %(sighting_id)s"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def edit_sighting(cls,data):
        query = """UPDATE sightings 
        SET what_happened = %(what_happened)s,
        location = %(location)s,
        date_sighted = %(date_sighted)s,
        number_of_squatches = %(number_of_squatches)s,
        updated_at = NOW()
        WHERE id = %(sighting_id)s"""
        return connectToMySQL(db).query_db(query, data)



