import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movies]
movie_titles.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for index, movie in enumerate(movie_titles, start=1):
        file.write(f"{index}) {movie}\n")