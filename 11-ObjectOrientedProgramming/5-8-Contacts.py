class contacts:
    def __init__(self,name, email, tel):
        self.name = name
        self.email = email
        self.tel = tel
    def __str__(self):
        return f'{self.name:<15}{self.email:<20}{self.tel}'
    