class User:
    def __init__(self, values):
        self.firstname = values["firstname"]
        self.lastname = values["lastname"]
        self.email = values["email"]
        self.password = values["password"]
        self.username = values["username"]
        
class File:
    def __init__(self):
        pass