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
            "fuel_capacity": car["fuel_capacity"],
            "registration_number": car["registration_number"],
            "vin": car["vin"],
            "mileage_id": car["mileage_id"],
            "user_id": car["user_id"]

        }
        self.collection.insert_one(query) 
        print("Added to DB " + str(query))

   #Zwracanie dokumentów "car" w formie listy
    def fetch_cars_from_db(self):
        
        cars = list(self.collection.find({}))
        return cars

#Tworzenie instancji klasy CarsHandler i przypisywanie jej do zmiennej "car", tworzenie słownika "car1"
car = CarsHandler()

car1 = {
    "name": "Volksawgen", 
    "mark": "VW",
    "year": 2003
    }

#dodawanie obiektu do bazy
car.add_car_to_db(car1)

#Wyświetlanie samochodów po roku produkcji
print(car["year"])

#Pobieranie listy samochodów z bazy, przypisanie wyniku do zmiennej cars
cars = car.fetch_cars_from_db()

#Wyświetlanie samochodów
print(cars)

#Pętla wyświetlająca dokument z kolekcji cars
for c in cars:
    print(f'{c["year"]} + {c["mark"]} + {c["name"]}')

#Pobranie z bazy samochodów danego użytkownika
user_id = ""
user_cars = car.fetch_user_cars(user_id)
print(f"\nUser {user_id} cars:")
for user_car in user_cars:
    print(user_car)

#Listowanie wszystkich samochodów w bazie danych
print("All cars in the database:")
car.list_all_cars()


# Pobranie posortowanych rosnąco samochodów według ceny
ascending_cars = car.fetch_cars_sorted_by_price(ascending=True)
print("Sorted ascending by price:")
for c in ascending_cars:
    print(f'name: {c["name"]}, price: {c["price"]}')

#Pobranie posortowanych malejąco samochodów według ceny
descending_cars = car.fetch_cars_sorted_by_price(ascending=False)
print("Sorted descending by price:")
for c in descending_cars:
    print(f'name: {c["name"]}, price: {c["price"]}')

# Zapytanie o samochód o podanym numerze rejestracyjnym
    def fetch_car_by_registration_number(self, registration_number):
        car = self.collection.find_one({"registration_number": registration_number})
        return car

# Pobranie z bazy samochodu po numerze rejestracyjnym
registration_number = ""
car_by_registration_number = car.fetch_car_by_registration_number(registration_number)
if car_by_registration_number:
    print("Car found:")
    print(car_by_registration_number)
else:
    print("Car not found for registration number:", registration_number)





