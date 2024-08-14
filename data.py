import requests
import json
import pandas as pd

response_API = requests.get('https://exnaton-public-s3-bucket20230329123331528000000001.s3.eu-central-1.amazonaws.com/challenge/95ce3367-cbce-4a4d-bbe3-da082831d7bd.json')
#print(response_API.status_code)
data_1 = response_API.text
data_1 = json.loads(data_1)
df=pd.DataFrame(data_1['data'])
print('data has been collected')