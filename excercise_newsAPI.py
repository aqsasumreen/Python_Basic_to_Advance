# --------------------Exercise#10------------------------
# news api
import requests
import json
#
query = input("What type of news you want ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-03-08&sortBy=publishedAt&apiKey=45af0f7255fd4e2b9846569af5e208d4"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:  # news is dictionary
    print(article["title"])
    print(article["description"])
    print("--------------------------------------------------")