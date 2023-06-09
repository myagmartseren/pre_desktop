class User:
    def __init__(self, values: dict):
        self.id = values.get("id")
        self.firstname = values.get("firstname")
        self.lastname = values.get("lastname")
        self.email = values.get("email")
        self.public_key = values.get("public_key")
        self.signer_key = values.get("signer_key")

        self.password = values.get("password")
        self.username = values.get("username")
        self.access_token = values.get("access_token")
        
class File:
    def __init__(self, values: dict):
        self.id = values.get("id")
        self.name = values.get("name")
        self.path = values.get("path")
        self.owner_id = values.get('owner_id')
        self.key = values.get('key')
        self.capsule = values.get('capsule')

class Share:
    def __init__(self, values: dict):
        self.id = values.get("id")
        self.file_id = values.get("file_id")
        self.delegator_id = values.get("delegator_id")
        self.delegatee_id = values.get('delegatee_id')
        self.rekey = values.get('rekey')