import requests

URL = "https://api.github.com"

def search_repositories(query):
    url = f"{URL}/search/repositories"
    params = {"q": query,"per_page": 5}
    response = requests.get(url, params=params)
    data = response.json()
    return data["items"]

def get_repository(owner, repo):
    url = f"{URL}/repos/{owner}/{repo}"
    response = requests.get(url)
    data = response.json()
    return data

def get_latest_release(owner, repo):
    url = f"{URL}/repos/{owner}/{repo}/releases/latest"
    response = requests.get(url)
    data = response.json()
    return data

def get_issues(owner, repo):
    url = f"{URL}/repos/{owner}/{repo}/issues"
    params = {"state": "open","per_page": 5}
    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_user(username):
    url = f"{URL}/users/{username}"
    response = requests.get(url)
    data = response.json()
    return data
