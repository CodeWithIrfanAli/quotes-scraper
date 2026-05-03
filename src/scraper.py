import requests
from bs4 import BeautifulSoup
import csv

url = "http://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

quotes = soup.find_all("div", class_="quote")

for q in quotes:
    text = q.find("span", class_="text").text
    author = q.find("small", class_="author").text

    quotes_data.append([text, author])

# Save to CSV
with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(quotes_data)

print("Data saved to quotes.csv")
