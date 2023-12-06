
#%%

import requests as r
import json
import webbrowser
import random 

api_key ="15clz3EppCwxet9dg6eXCqUkPktpLk4kb5M1Q0c2"
api_url = "https://api.nasa.gov/planetary/apod"

year = str(random.randint(2000,2022))
month = str(random.randint(1,12))
day = str(random.randint(1,28))
date = year + "-" + month + "-" + day
# print(date)

#Params
params = {
    'api_key':api_key,
    'hd':'True',
    # 'date':'2022-11-02'
    'date':date
}

response = r.get(api_url,params=params)
json_data = json.loads(response.text)
# print(json_data)
image_url = json_data['url']
print(json_data['date'])
print(json_data['title'])
print(json_data['explanation'])
print(json_data['url'])

webbrowser.open(image_url)








# %%
