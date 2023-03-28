from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.id = data['id']
        self.ninjas_dojo = data['dojo_id']

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) ) #creating a list of ninja instances
        return ninjas

    @classmethod
    def create_ninja(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) 
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW())"""
        return  connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def delete_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        return  connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def edit_ninja(cls, data):
        query = """UPDATE users
        SET first_name = %(first_name)s, 
        last_name = %(last_name)s, 
        age = %(age)s,
        dojo_id = %(dojo_id)s
        WHERE id = %(id)s;"""
    

