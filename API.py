import urllib.request as request
import json 

with request.urlopen("https://data.cityofchicago.org/resource/dw27-rash.json") as response:
    source = response.read() 
    data = json.loads(source)

with request.urlopen("https://data.cityofchicago.org/resource/9xs2-f89t.json") as response_1:
    source_1 = response_1.read() 
    data_1 = json.loads(source_1)

