from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for one_dojo in results:
            dojos.append( cls(one_dojo) )
        return dojos

    @classmethod
    def create_dojo(cls, data):
        #check here for error not including id
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES ( %(dojo_name)s, NOW(), NOW() );"
        return  connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_dojos_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        dojo = cls( results[0] )
        for row in results:
            data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojo_id' : row['dojo_id']
            }
            dojo.ninjas.append( Ninja(data) )
        return dojo

    @classmethod
    def delete_dojo(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        return  connectToMySQL('dojos_and_ninjas').query_db(query, data)
        
