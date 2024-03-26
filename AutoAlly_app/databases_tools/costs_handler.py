from mongodb_handler import MongoDB


class CostsHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("costs")