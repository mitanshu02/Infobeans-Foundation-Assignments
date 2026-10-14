import requests

URL = "https://api.stackexchange.com/2.3"

def search_questions(query):
    url = f"{URL}/search/advanced"
    params = {"site": "stackoverflow","q": query,"sort": "relevance","pagesize": 5}
    response = requests.get(url, params=params)
    data = response.json()
    return data["items"]


# if __name__ == "__main__":
#     questions = search_questions("how to reverse a list in python")
#     for question in questions:
#         print(f"\nTitle: {question['title']}")
#         print(f"Score: {question['score']}")
#         print(f"Answers: {question['answer_count']}")
#         print(f"URL: {question['link']}")