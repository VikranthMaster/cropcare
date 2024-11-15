import requests
from bs4 import BeautifulSoup

find = input()

url = f'https://www.google.com/search?q={find}'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
mysearch = soup.find("div", class_="BNeawe").text
print(mysearch)


