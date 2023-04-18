import requests
from bs4 import BeautifulSoup
import webbrowser

response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find(id='firstHeading').text
print("Tytuł artykułu: " + title)
decyzja = input("Czy chcesz otworzyć ten artykuł w przeglądarce? (tak/nie) ")
if decyzja.lower() == 'tak':
    url = response.url
    print(url)
    webbrowser.open(url, new=1)
else:
    print("Nie otwarto artykułu.")