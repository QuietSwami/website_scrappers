
# Class to create houses to insert into the data storage.
import datetime
import csv

class House:

    def __init__(self):
        self.price = 0
        self.location = ''
        self.title = '' 
        self.sqr_m = 0
        self.rooms = 0
        self.energy_consumption = 0
        self.years = 0

    def get_years(self):
        return self.years
    
    def set_years(self, construction_year) :
        now = datetime.datetime.now()
        self.years = now.year - construction_year

    def get_energy_consumption(self):
        return self.energy_consumption
    
    def set_energy_consumption(self, energy_consumption) :
        self.energy_consumption = energy_consumption

    def get_rooms(self):
        return self.rooms
    
    def set_rooms(self, rooms):
        self.rooms = rooms

    def get_sqr_m(self):
        return self.sqr_m
    
    def set_sqr_m(self, sqr_m):
        self.sqr_m = sqr_m

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location
    
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price

    def __repr__(self):
        return 'House(%s, %s, %s, %s, %s, %s, %s)' %(self.price, self.location, self.title, self.sqr_m, self.rooms, self.energy_consumption, self.years)

    def _to_csv(self, file_name):
        with open(file_name, 'w') as csv_writter:
            writer = csv.writer(csv_writter)
            writer.writerow([self.price, self.location, self.sqr_m, self.rooms, self.years, self.energy_consumption, self.title])

    # There should be a way to use the __dict__atribute, or use dict(House)
    def _to_dict(self):
        return {'price': self.price, 'location': self.location, 'sqr_m': self.sqr_m, 'rooms': self.rooms, 'energy_consumption': self.energy_consumption, \
            'years': self.years, 'title': self.title}
     