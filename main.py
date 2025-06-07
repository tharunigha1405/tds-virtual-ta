import requests
from bs4 import BeautifulSoup

url = "https://tds.s-anand.net/#/2025-01/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

with open("data/course/tds_content.html", "w", encoding='utf-8') as f:
    f.write(soup.prettify())
