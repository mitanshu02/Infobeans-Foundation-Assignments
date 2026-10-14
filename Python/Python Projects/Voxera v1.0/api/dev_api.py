import requests

URL = "https://dev.to/api"

def search_articles(query):
    url = f"{URL}/articles/search"

    params = {"q": query,"per_page": 5}
    response = requests.get(url, params=params)
    data = response.json()

    return data
