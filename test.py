import requests
api_key = "AIzaSyBRoEH_BsBpaxrcqy0dmmk52X5q8QtDm1I"
country_codes = "US"

request_url = f"https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode={country_codes}&key={api_key}"
request = requests.get(request_url)
title = request.json().get('items')
title_dict = {}
for name in title:
    title_dict[int(name["id"])] = name["snippet"]["title"]
a = 2
for i in title_dict:
    if a == i:
        print(title_dict[i])