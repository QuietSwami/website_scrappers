from bs4 import BeautifulSoup
import requests
import csv


def request_page(link):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    r = requests.get(link, headers=headers)
    return BeautifulSoup(r.text, 'html.parser')

def create_link(base_link, location, job_description):
    j = job_description.split(' ')
    return base_link + 'jobs?q=' + j[0] + '+' + j[1] + '&l=' + location

def get_next_page(base_link, page_number):
    return base_link + '&start=' + str(page_number*10)

def get_number_of_pages(base_soup, number_entries):
    return int(int(base_soup.find('div', {'id': 'searchCount'}).text.rstrip("\n\r").split(' ')[-2].replace(',',''))/number_entries)

if __name__ == "__main__":
    base = 'http://indeed.ca/'
    base_link = create_link(base, 'Toronto', 'software developer')
    print(base_link)
    # # base_soup = request_page(base_link)
    # number_pages = get_number_of_pages(base_soup, 20)

    for i in range(2, 20, 2):
        print(get_next_page(base_link, i))