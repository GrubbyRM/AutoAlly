from mongodb_handler import MongoDB


class ContactsHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("contacts")