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
            "notes": cost["notes"]
        }