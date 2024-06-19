from mysqlconnection import connecttoMysql

class Pet:
    def __init__(self, data):
        self.id = data['id']
        self.petname = data['petname']
        self.pettype = data['pettype']
        self.petdesc = data['petdesc']
        self.petskill1 = data['petskill1']
        self.petskill2 = data['petskill2']
        self.petskill3 = data['petskill3']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getall_pets(cls):
        query = """
        SELECT id, petname, pettype, petdesc, petskill1, petskill2, petskill3, created_at, updated_at 
        FROM pets
        """
        results = connecttoMysql("market_db").query_db(query)
        pets = []
        for pet in results:
            pets.append(cls(pet))  # Create instances of Pet
        return pets

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT id, petname, pettype, petdesc, petskill1, petskill2, petskill3, created_at, updated_at 
        FROM pets
        WHERE id = %(id)s
        """
        result = connecttoMysql("market_db").query_db(query, data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def new_pet(cls, data):
        query = """
        INSERT INTO pets (petname, pettype, petdesc, petskill1, petskill2, petskill3) 
        VALUES (%(petname)s, %(pettype)s, %(petdesc)s, %(petskill1)s, %(petskill2)s, %(petskill3)s)
        """
        return connecttoMysql("market_db").query_db(query, data)
