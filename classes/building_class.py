class Building:
    """Building class documentation"""

    def __init__(self, building_type='Not specified', owner='Not specified', number_of_floors='Not specified',
                 number_of_rooms='Not specified', square='Not specified', price='Not specified',
                 address='Not specified', year_of_construction='Not specified'):
        """constructor"""
        self.building_type = building_type
        self.owner = owner
        self.number_of_floors = number_of_floors
        self.number_of_rooms = number_of_rooms
        self.square = square
        self.price = price
        self.address = address
        self.year_of_construction = year_of_construction

    def get_info(self, get_as_dic=False):
        """get information about this building"""
        features = {'Building type': self.building_type,
                    'Owner': self.owner,
                    'Number of floors': self.number_of_floors,
                    'Number of rooms': self.number_of_rooms,
                    'Square': self.square,
                    'Price': self.price,
                    'Address': self.address,
                    'Year of construction': self.year_of_construction}
        if get_as_dic:
            return features
        for i in features:
            print(f'{i} is {features[i]}')

    def build(self):
        """build this building"""
        return f"This {self.building_type} was successfully built"

    def buy(self):
        """buy this building"""
        return f"This {self.building_type}  was successfully bought for {self.price}"

    def sell(self):
        """sell this building"""
        if self.owner == 'state':
            return f"""
            You tried to sell {self.building_type} belonging to the state, young Atlas Shrugged.
            You can not sell the government property. Your IP address has been recorded.
            Stay where you are until the police arrive
            """
        return f"This {self.building_type}  was successfully sold for {self.price}"


if __name__ == "__main__":
    house1 = Building("house", "Ivanov", 2, 5, 120, 7990000, "Lenina 1", 2010)
    print(house1.buy())
    house1.get_info()
    print(house1.get_info(get_as_dic=True))
    print(house1.buy())
    print(house1.sell())
    print()
    house2 = Building(building_type="house", owner="Petrov", square=84, address="Lenina 24")
    print(house2.build())
    house2.get_info()
    print()
    school = Building(building_type="school", owner="state", number_of_floors=4, address="Lenina 12",
                      year_of_construction=1983)
    school.get_info()
    print(school.sell())
