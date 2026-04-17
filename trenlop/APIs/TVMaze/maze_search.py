import requests

## Data exploration
keyword = "comedy"
req = "https://api.tvmaze.com/search/shows?q=" + keyword
res = requests.get(req).json()

genre_occurance = {}

for phim in res:
    for genre in phim["show"]["genres"]:
        if genre not in genre_occurance: 
            print(f"{genre} not in occurance yet, adding...")
            genre_occurance[genre] = 1
            print("added")
        elif genre in genre_occurance: 
            print(f"{genre} is in occurance, incrementing...")
            genre_occurance[genre] += 1
            print("incremented")

print(genre_occurance)

    
