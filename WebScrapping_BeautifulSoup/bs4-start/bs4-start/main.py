from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all("a")

for tag in all_anchor_tags:
    print(tag.get("href"))