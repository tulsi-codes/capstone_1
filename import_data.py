import requests
from bs4 import BeautifulSoup
import pandas as pd 

 
url = 'https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

for link in soup.find_all('a'):
    if "trip+data/yellow_tripdata_2020-01" in link.get('href'): 
       link = link.get('href')
       df = pd.read_csv(link)
       print(df)


