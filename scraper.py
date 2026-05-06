import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

blocks = soup.find_all("div", class_="quote")

data = []

for block in blocks:
    text = block.find("span", class_="text").text
    author = block.find("small", class_="author").text

    data.append({"quote": text, "author": author})
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
      writer = csv.DictWriter(file, fieldnames=["quote", "author"])

      writer.writeheader()
      writer.writerows(data)

print("Scraping completed and saved to quotes.csv")