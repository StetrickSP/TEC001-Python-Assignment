import requests

keyword = input("Enter keyword: ")

req = "https://api.tvmaze.com/search/shows?q=" + keyword
res = requests.get(req).json()
print(res)