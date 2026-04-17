import requests

class TVShow:
    def __init__(self, name, language, rating):
        self.name = name
        self.language = language
        self.rating = rating

    def is_highly_rated(self):
        if self.rating > 8: return True

req1 = "https://api.tvmaze.com/singlesearch/shows?q=girls"
req2 = "https://api.tvmaze.com/singlesearch/shows?q=the%20boys"

res1 = requests.get(req1).json()
res2 = requests.get(req2).json()

TVShow1 = TVShow(res1["name"], res1["language"], res1["rating"])
TVShow2 = TVShow(res2["name"], res2["language"], res2["rating"])

print(TVShow1)
print(TVShow2)

