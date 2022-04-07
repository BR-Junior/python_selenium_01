import requests
from bs4 import BeautifulSoup

response = requests.get('https://statusinvest.com.br/acoes/busca-avancada')

content = response.content

soup = BeautifulSoup(content, 'html.parser') # vai retornao conteudo HTML do pagina, transforama num objeto do soup

#print(site.prettify()) # .prettify traz o conteudo de forma organizada

#page = site.find('div', attrs={'class': 'card'}) # find é para procuar um teg no codigo, attrs = a atributo: find('tag', attrs={'class': 'nome da classs'})

print(soup.prettify())

#como achar coisas dentro de outras 

noticias = soup.find('tag', attrs={'class': 'nome da clase'})

titolo_da_noticias = noticias.find('tag', attrs={'classe ou div': 'nome da clase'}) 