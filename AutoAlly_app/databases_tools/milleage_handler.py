from mongodb_handler import MongoDB

class MilleageHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("milleage")

    def add_milleage_to_db(self, milleage):
        query = {
            "actual": milleage["actual"],
            "historicaly": milleage["historicaly"],
            "date": milleage["date"],
            "car_id": milleage["car_id"]

        }