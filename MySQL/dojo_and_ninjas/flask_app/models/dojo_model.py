from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model
from flask_app import DATABASE

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # DISPLAY ALL ninjas from a dojo
    @classmethod
    def get_all_ninja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            dojo_instance = cls(results[0])
            ninja_list = []
            for row_in_db in results:
                ninja_data = {
                    **row_in_db,
                    'id': row_in_db['ninjas.id'],
                    # 'first_name': row_in_db['ninjas.first_name'], 
                    # 'last_name': row_in_db['ninjas.last_name'],
                    # 'age': row_in_db['ninjas.age'],
                    'created_at': row_in_db['ninjas.created_at'],
                    'updated_at': row_in_db['ninjas.updated_at']
                }
                ninja_instance = ninja_model.Ninja(ninja_data)
                ninja_list.append(ninja_instance)
            dojo_instance.list_ninjas = ninja_list
            return dojo_instance
        return results


    # READ ALL dojos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for ninja in results:
            dojos.append( cls(ninja) )
        return dojos


    # ADD NEW dojo
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES ( %(name)s);"
        return connectToMySQL(DATABASE).query_db( query, data )


    # ADD NEW ninja
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES ( %(name)s);"
        return connectToMySQL(DATABASE).query_db( query, data )
