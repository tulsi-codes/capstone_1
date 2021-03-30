import requests
from bs4 import BeautifulSoup
 
 #loads url text 
 
url = 'https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
#parses info to find links 

#keeps count of links to double check work 
count = 0


for link in soup.find_all('a'):  #finds links
    if "trip+data/yellow_tripdata_" in link.get('href'):    #find yellow cab data 
        print(link.get('href'))        
        count += 1 # takes count
print(count)   

