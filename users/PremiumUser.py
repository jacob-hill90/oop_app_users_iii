from users.User import User

class PremiumUser(User):
    tier = 'premium'

    def __init__(self, name, email, id_number, major, year_born):
        super().__init__(name, email, id_number, major, year_born)
