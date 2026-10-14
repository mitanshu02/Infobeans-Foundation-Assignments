import requests
from config import NEWS_API_KEY

URL = "https://newsapi.org/v2/everything"

def get_news():
    params = {"q": "technology OR artificial intelligence OR software OR cybersecurity","language": "en","sortBy": "relevancy","pageSize": 5,"apiKey": NEWS_API_KEY}
    response = requests.get(URL, params=params)
    data = response.json()
    return data["articles"]
