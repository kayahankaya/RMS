import datetime

class UserEntity:

    def __init__(self):
        self.user_id = 0
        self.lastname = ''
        self.firstname = ''
        self.username = ''
        self.password = ''
        self.created_at = datetime.date(2002,6,12)
        self.updated_at = datetime.date(2002,6,12)