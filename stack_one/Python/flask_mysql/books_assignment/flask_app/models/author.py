from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self,data):
        self.name = data['name']
        self.favorites = []
        self.id = data['id']
    
    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return  connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for a in results:
            authors.append( cls(a) )
        return authors
