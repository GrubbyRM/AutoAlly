from mongodb_handler import MongoDB

class PhotosHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("photos")

    def add_photos_to_db(self, photos):
        query = {
            "photo": photos["photo_name"],
            "type": photos["photo_type"],
            "type_id": photos["type_id"],
            "car_id": photos["car_id"]


        }