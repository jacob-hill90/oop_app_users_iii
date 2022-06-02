from users.User import User

class FreeUser(User):
    
    tier = 'free'
    
    def __init__(self, name, email, id_number, major, year_born):
        super().__init__(name, email, id_number, major, year_born)
        self.post_count = 0
        