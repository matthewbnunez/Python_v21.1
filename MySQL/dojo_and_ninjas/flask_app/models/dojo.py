from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    # READ ALL dojos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for ninja in results:
            dojos.append( cls(ninja) )
        return dojos


    # ADD NEW dojo
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES ( %(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )


    # ADD NEW ninja
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES ( %(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
