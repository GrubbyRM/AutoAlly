from mongodb_handler import MongoDB


class InspectionsHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("inspections")

    def add_inspections_to_db(self, isnpection):
        query = {
            "type": inspection["type"],
            "result": inspection["result"],
            "date": inspection["date"]
            "garage_name": isnpection["garage_name"],
            "car_id": isnpection["car_id"],
            "contact_id": isnpection["contact_id"],
            "comment": isnpection["comment"]
        }