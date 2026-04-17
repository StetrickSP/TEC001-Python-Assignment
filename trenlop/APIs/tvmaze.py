import requests
import pprint as pretty

keyword = input("Enter keyword: ")

req = "https://api.tvmaze.com/search/shows?q=" + keyword
res = requests.get(req).json()
for item in res:
    pretty.pprint(item['show']['schedule']['days'])
