# Imovirtual House Scraper.

from bs4 import BeautifulSoup
import requests

class Idealista:

    base_link = 'http://www.idealista.pt'
    
    def __init__(self, type='rent', city='Lisboa', location='Benfica', house_type='apartmento', price_range=None, tipology=None, sqr_m_range=None, radius=0):
        """
            - Price Range and Square Meters:  A list with 2 values, the smallest can be 0.
        """
        if type == 'rent':
            self.type = 'arrendar-casas'
        elif type == 'buy':
            self.type = 'comprar-casas'
        self.house_type = house_type
        self.city = city.lower()
        self.location = location.lower()
        if price_range != None:
            self.price_range = price_range.sort()
        else:
            self.price_range = None
        self.tipology = tipology
        if sqr_m_range != None:
            self.sqr_m_range = sqr_m_range
        else:
            self.sqr_m_range= None
        self.radius = radius

    def create_link(self):
        new_link = __class__.base_link + '/' + self.type + '/' + self.city + '/' + self.location  
        
        if self.sqr_m_range != None or self.tipology != None or self.price_range != None:
            new_link += '/com-'
            
        if self.price_range != None:
            small = 'preco-min_' + str(self.price_range[0])
            big = 'preco-max_' + str(self.price_range[1])
            new_link += small + ',' + big + ','

        if self.tipology != None:
            new_link += 't' + str(self.tipology)
        
        if self.sqr_m_range != None:
            small = 'tamanho-min_' + str(self.sqr_m_range[0])
            big = 'tamanho-max_' + str(self.sqr_m_range[1])
            new_link += small + ',' + big + ','

        return new_link

    def get_webpage(self, link):
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}
        r = requests.get(link, headers=header)
        return r.text


if __name__ == "__main__":
    i = Idealista()
    print(i.get_webpage(i.create_link()))