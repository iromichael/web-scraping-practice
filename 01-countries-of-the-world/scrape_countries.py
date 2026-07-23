import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.scrapethissite.com/pages/simple/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

countries = soup.find_all('div', class_='country')

country_names = []
capitals = []
popuplations = []
areas = []

for country in countries:
    country_name = country.find('h3', class_='country-name').get_text(strip=True)
    capital = country.find('span', class_='country-capital').get_text(strip=True)
    popuplation = country.find('span', class_='country-population').get_text(strip=True)
    area = country.find('span', class_='country-area').get_text(strip=True)
    
    country_names.append(country_name)
    capitals.append(capital)
    popuplations.append(popuplation)
    areas.append(area)

df = pd.DataFrame({'Countries': country_names, 'Capitals': capitals, 'Population': popuplations, 'Area (km)': areas})


df.to_csv('countries_of_the_world.csv', index=False)