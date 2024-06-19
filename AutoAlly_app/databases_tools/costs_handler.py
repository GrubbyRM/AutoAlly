from mongodb_handler import MongoDB


class CostsHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("costs")


    def add_costs_to_db(self, cost):
        query = {
            "sum": cost["sum"],
            "payment_status": cost["payment_status"],
            "payment_method": cost["payment_method"],
            "responsible person": cost["responsible person"],
            "date": cost["date"],
            "cost_id": cost["cost_id"],
            "car_id": cost["car_id"],
            "photo_id": cost["photo_id"],
            "mileage_id": cost["mileage_id"]

        }