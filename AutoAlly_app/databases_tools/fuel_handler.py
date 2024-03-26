from mongodb_handler import MongoDB


class FuelHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("fuel")

    def add_fuel_to_db(self, fuel):
        query = {
            "type": car["type"]
        }
        self.collection.insert_one(query)
        print("Added to DB " + str(query))