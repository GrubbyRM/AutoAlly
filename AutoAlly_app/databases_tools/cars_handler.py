from databases_tools.mongodb_handler import MongoDB

class CarsHandler(MongoDB):
    
    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("cars")