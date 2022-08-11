from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    # READ ALL ninjas
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas


    # READ ONE ninja
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        if results:
            ninja_instance = cls(results[0])
            return ninja_instance
        return results


    # ADD NEW ninja
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name , age , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )


    # UPDATE ninja
    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s , age = %(age)s, updated_at = NOW()" \
            "WHERE id = %(id)s"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )


    # DELETE USER
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )