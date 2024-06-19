from mongodb_handler import MongoDB

class ReminderHandler(MongoDB):

    def __init__(self):
        super().__init__()
        self.collection = self.get_collection("reminder")

    def add_reminder_to_db(self, reminder):
        query = {
            "type": reminder["type"],
            "type_id": reminder["type_id"],
            "start_date": reminder["start_date"],
            "end_date": reminder["end_date"],
            "notification_type": reminder["notification_type"]
        }