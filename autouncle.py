from bs4 import BeautifulSoup
import requests
import csv
import os

def get_directory_page(soup):
    '''
    Returns all the car listings in one page
    '''
    a = []
    for i in soup.find_all('div', {'class': 'listing-item-car-details-headline-wrapper'}):
        a.append(i.a['href'])
    return a

def get_car_page(car_link):
    r = requests.get(car_link)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_car_info(carpage):
    headline = carpage.find('h1', {'class': 'car-headline'}).text.rstrip("\n\r").split(' ')
    make = headline[0].rstrip("\n\r").replace('\n', '')
    model = headline[1]
    year = 0
    km = 0
    gear = ''
    cc = ''
    hp = 0
    price = int(carpage.find('span', {'class': 'price right'}).text.split(' ')[1].replace(',','').rstrip("\n\r").replace('\n', ''))
    for i in carpage.find_all('div', {'class': 'car-data__group-info'}):
        if i.find('p').text == 'Year':
            year = int(i.find('span').text)
        elif i.find('p').text == 'Km':
            km = int(i.find('span').text.replace(',',''))
        elif i.find('p').text == 'Gear':
            gear = i.find('span').text.rstrip("\n\r").replace('\n', '')
        elif i.find('p').text == 'Engine':
            if i.find('small') != None:
                hp =  int(i.find('small').text.split(" ")[0].replace('\n', ''))
                cc = float(i.find('span').text.split(' ')[0].replace('\n', ''))
            else:
                cc = float(i.find('span').text.split(' ')[0].replace('\n', ''))

    return [make, model, year, km, gear, cc, hp, price]

def save_car_info(info, file_name): 
    '''
    Info is the list given by get_car_info 
    '''
    with open(file_name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(info)

def get_directory_next_page(base, page_number):
    return base + '&page=' + str(page_number)

def get_car_link(car_link):
    return 'https://www.autouncle.pt' + car_link 

if __name__ == "__main__":
    
    # Case 1: Diesel Cars with less of 100000 km  
    au = 'https://www.autouncle.pt/en/cars_search?s[min_year]=2004&s[max_km]=100000&s[fuel_types]=Diesel'
    case1 = 'Petrol_100000_Nac.csv'
    with open(case1, 'w') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['Make', 'Model', 'Year', 'Km', 'Gear', 'CC', 'HP', ' Price'])

    for i in range(1,21):
        if i == 1:
            r = requests.get(au)
            soup = BeautifulSoup(r.text, 'html.parser')
            page = get_directory_page(soup)
            for i in page:
                save_car_info(get_car_info(get_car_page(get_car_link(i))), case1)
        else:
            r = requests.get(get_directory_next_page(au, i))
            soup = BeautifulSoup(r.text, 'html.parser')
            page = get_directory_page(soup)
            for i in page:
                save_car_info(get_car_info(get_car_page(get_car_link(i))), case1)

    # Case 2: Diesel Cars with less of 200000 km and more than 100000  
    au = 'https://www.autouncle.pt/en/cars_search?s[min_year]=2004&s[min_km]=100000&s[max_km]=200000&s[fuel_types]=Diesel'
    case1 = 'Diesel_200000_Nac.csv'
    with open(case1, 'w') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['Make', 'Model', 'Year', 'Km', 'Gear', 'CC', 'HP', ' Price'])

    for i in range(1,21):
        if i == 1:
            r = requests.get(au)
            soup = BeautifulSoup(r.text, 'html.parser')
            page = get_directory_page(soup)
            for i in page:
                save_car_info(get_car_info(get_car_page(get_car_link(i))), case1)
        else:
            r = requests.get(get_directory_next_page(au, i))
            soup = BeautifulSoup(r.text, 'html.parser')
            page = get_directory_page(soup)
            for i in page:
                save_car_info(get_car_info(get_car_page(get_car_link(i))), case1)
    
    # Case 3: Petrol Cars with less of 100000 km  
    au = 'https://www.autouncle.pt/en/cars_search?s[min_year]=2004&s[max_km]=100000&s[fuel_types]=Benzin'
    case1 = 'Petrol_100000_Nac.csv'
    with open(case1, 'w') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['Make', 'Model', 'Year', 'Km', 'Gear', 'CC', 'HP', ' Price'])

    for i in range(1,21):
        if i == 1:
            r = requests.get(au)
            soup = BeautifulSoup(r.text, 'html.parser')
            page = get_directory_page(soup)
            for i in page:
                save_car_info(get_car_info(get_car_page(get_car_link(i))), case1)
        else:
            r = requests.get(get_directory_next_page(au, i))
            soup = BeautifulSoup(r.text, 'html.parser')
            page = get_directory_page(soup)
            for i in page:
                save_car_info(get_car_info(get_car_page(get_car_link(i))), case1)

    # Case 4: Petrol Cars with less of 200000 km and more than 100000  
    au = 'https://www.autouncle.pt/en/cars_search?s[min_year]=2004&s[min_km]=100000&s[max_km]=200000&s[fuel_types]=Benzin'
    case1 = 'Diesel_200000_Nac.csv'
    with open(case1, 'w') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['Make', 'Model', 'Year', 'Km', 'Gear', 'CC', 'HP', ' Price'])

    for i in range(1,21):
        if i == 1:
            r = requests.get(au)
            soup = BeautifulSoup(r.text, 'html.parser')
            page = get_directory_page(soup)
            for i in page:
                save_car_info(get_car_info(get_car_page(get_car_link(i))), case1)
        else:
            r = requests.get(get_directory_next_page(au, i))
            soup = BeautifulSoup(r.text, 'html.parser')
            page = get_directory_page(soup)
            for i in page:
                save_car_info(get_car_info(get_car_page(get_car_link(i))), case1)

                       