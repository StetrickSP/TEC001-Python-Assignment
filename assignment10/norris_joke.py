import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data["value"])  # only print the joke text
    else:
        print("Failed to fetch joke.")

get_chuck_norris_joke()