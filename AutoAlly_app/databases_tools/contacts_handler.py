from mongodb_handler import MongoDB


class ContactsHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("contacts")

    def add_contact_to_db(self, contact):
        query = {
            "name": contact["name"],
            "surname": contact["surname"],
            "company": contact["company"],
            "city": contact["city"],
            "address": contact["address"]
        }