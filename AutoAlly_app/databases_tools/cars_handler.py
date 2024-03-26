from mongodb_handler import MongoDB

class CarsHandler(MongoDB):
    
    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("cars")

    def add_car_to_db(self, car):
        query = {
            "name": car["name"], 
            "mark": car["mark"],
            "year": car["year"],
            "engine_model": car["engine_model"],
            "color": car["color"],
            "first_registration_date": car["first_registration_date"],
            "tank_capacity": car["tank_capacity"],
            "registration_number": car["registration_number"],
            "vin": car["vin"]

        }
        self.collection.insert_one(query) 
        print("Added to DB " + str(query))
        
    def fetch_cars_from_db(self):
        
        cars = list(self.collection.find({}))
        return cars

car = CarsHandler()

car1 = {
    "name": "Volksawgen", 
    "mark": "VW",
    "year": 2003
    }
#print(car["year"]) 

#car.add_car_to_db(car1)  #dodawanie obiektu do bazy

#cars = car.fetch_cars_from_db()
#print(cars)

#Pętla wyświetlająca dokument z kolekcji cars
#for c in cars:
#print(f'{c["year"]} + {c["mark"]} + {c["name"]}')





