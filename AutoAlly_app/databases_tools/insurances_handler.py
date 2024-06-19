from mongodb_handler import MongoDB
from mongodb_handler import json

class InsurancesHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("insurances")

    def add_insurances_to_db(self, insurances):
        query = {
            "insuracer_name": incurances["insuracer_name"],
            "insurance_date":  insurances["insurance_date"],
            "insurance_price": insurances["insurance_price"],
            "insurance_details": json.loads(insurances["insurance_detail"]),
            "car_id": insurances["car_id"],
            "contacts_id": insurances["contacts_id"]

        }