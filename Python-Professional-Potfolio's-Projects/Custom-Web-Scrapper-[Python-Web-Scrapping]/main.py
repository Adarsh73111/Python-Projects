import requests
from bs4 import BeautifulSoup
import csv


def scrape_hacker_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("tr", class_="athing")
    scraped_data = []

    for article in articles:
        title_element = article.find("span", class_="titleline").find("a")
        title = title_element.text
        link = title_element.get("href")

        next_row = article.find_next_sibling("tr")
        score_element = next_row.find("span", class_="score")
        score = int(score_element.text.replace(" points", "")) if score_element else 0

        scraped_data.append({"Title": title, "Link": link, "Score": score})

    scraped_data = sorted(scraped_data, key=lambda x: x["Score"], reverse=True)

    filename = "hacker_news_top_articles.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Link", "Score"])
        writer.writeheader()
        writer.writerows(scraped_data)

    print(f"Successfully scraped {len(scraped_data)} articles and saved to {filename}")


if __name__ == "__main__":
    scrape_hacker_news()