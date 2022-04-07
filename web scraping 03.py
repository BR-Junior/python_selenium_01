import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias =[]

response = requests.get('https://g1.globo.com/')
content = response.content
soup = BeautifulSoup(content, 'html.parser')

# HTML da notícia
#noticia = soup.find('div', attrs={'class': 'feed-post-body'})

noticias = soup.findAll('div', attrs={'class': 'feed-post-body'})

#Título, bunscando conteudo dentro de outro
#titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

# Como percorer uma lista de noícias
for noticia in noticias:
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    # print(titulo.text)
    # print(titulo['href']) #para acessar o tributo da tag usa o [], como se fose um lista
    # print()
    lista_noticias.append([titulo.text, titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Títolo', 'Link'])

news.to_csv('lista.csv', index=False)

