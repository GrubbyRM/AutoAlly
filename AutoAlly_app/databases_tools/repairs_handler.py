from mongodb_handler import MongoDB

class RepairsHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("repairs")

    def add_repairs_to_db(self, repairs):
        query = {
            "type": repairs["type"],
            "comment": repairs["comment"],
            "car_id": repairs["car_id"],
            "costs": repairs["costs"],

        }