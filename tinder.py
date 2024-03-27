import requests
from bs4 import BeautifulSoup

url = 'https://tinder.com/@'


with open("usernames.txt", "r") as file:

    for perfil in file:
        perfil = perfil.strip()
        url_perfil = url + perfil
        response = requests.get(url_perfil)
        html = response.text

        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.text
        
        if title  == "Tinder | Dating, Make Friends & Meet New People":
            print("Perfil não encontrado")
        else:
            print('Perfil encontrado: ',url_perfil)