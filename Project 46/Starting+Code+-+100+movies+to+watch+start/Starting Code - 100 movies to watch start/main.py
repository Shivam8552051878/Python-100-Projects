import html

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
# print(soup.prettify())
data = soup.find_all(name='h3', class_="title")

list_movie = [movie.getText() for movie in data]
list_movie = list_movie[::-1]
print(list_movie)

with open("100_movie_solution.txt", "w", encoding="utf-8") as file:
    for movie in list_movie:
        file.write(f"{movie}\n")




# for move_name in data:
#     if len(move_name.text.split(")")) > 1:
#         top = move_name.text.split(")")[0]
#         move_name = move_name.text.split(")")[1].strip()
#         list_movie.append({"rank": int(top),
#                            "movie":move_name
#                            })
# list_movie_top = [ list_movie[98 - data] for data in range(len(list_movie))]
#
# with open("movie.txt" , "a") as file:
#     for movie in list_movie_top:
#         file.write(str(f"{movie['rank']}) {movie['movie']}".encode("utf8")))
#         file.write("\n")