class User:
    def __init__(self, values: dict):
        self.id = values.get("id")
        self.firstname = values.get("firstname")
        self.lastname = values.get("lastname")
        self.email = values.get("email")
        self.password = values.get("password")
        self.username = values.get("username")
        
class File:
    def __init__(self, values: dict):
        self.id = values.get("id")
        self.name = values.get("name")
        self.path = values.get("path")
        self.owner_id = values.get('owner_id')
        self.key = values.get('key')