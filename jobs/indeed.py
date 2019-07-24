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

def get_listings(page_soup):
    """
    Returns a list of listing in a page, as the ID of the listing.
    """ 
    job_listings = page_soup.find_all('div', {'class': 'jobsearch-SerpJobCard'})
    return [i['data-jk'] for i in job_listings]


def get_extended_listing_link(jk):
    return 'https://www.indeed.ca/viewjob?jk=' + jk

def get_listing_info(page_soup):
    """
    This returns a list containing the entries to the csv.
    """
    location = page_soup.find('div', {'class': 'location'}).text
    salary = page_soup.find('div', {'class': 'salary'}).text
    company = page_soup.find('div', {'class': 'company'}).text
    
if __name__ == "__main__":
    base = 'http://indeed.ca/'
    base_link = create_link(base, 'Toronto', 'software developer')
    print(base_link)
    with open('indeed_Toronto.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Company', 'Location', 'Salary', 'Title', 'Main Language'])
    for i in get_listings(request_page(base_link)):
        writer.writerow(get_listing_info(request_page(get_extended_listing_link(i))))
    writer.close()
    print('Dataset Concluded')
