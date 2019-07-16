# Imovirtual House Scraper.

from bs4 import BeautifulSoup
import requests

class Idealista:

    base_link = 'www.idealista.pt'
    
    def __init__(self, type='rent', location, house_type='apartmento', price_range=None, tipology=0, sqr_m_range=None, radius=0):
        """
            - Price Range and Square Meters:  A list with 2 values, the smallest can be 0.
        """
        if type == 'rent':
            self.type = 'arrendar'
        elif type == 'buy':
            self.type = 'comprar'
        self.house_type = house_type
        self.location = location.lower()
        self.price_range = price_range.sort()
        self.tipology = tipology
        self.sqr_m_range = sqr_m_range
        self.radius = radius

    def create_link(self):
        return None


if __name__ == "__main__":
    pass