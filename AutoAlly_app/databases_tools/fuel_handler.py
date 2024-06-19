from mongodb_handler import MongoDB


class FuelHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("fuel")

    def add_fuel_to_db(self, fuel):
        query = {
            "type": fuel["type"],
            "ammount": fuel["ammount"],
            "price": fuel["price"],
            "price_per_liter": fuel["price_per_liter"],
            "petrol_station": fuel["petrol_station"],
            "location": fuel["location"],
            "mileage_id": fuel["mileage_id"],
            "date": fuel["date"],
            "car_id": fuel["car_id"]

        }
        self.collection.insert_one(query)
        print("Added to DB " + str(query))