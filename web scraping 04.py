from tkinter import N
import requests
from bs4 import BeautifulSoup
import pandas as pd

url_base = 'https://lista.mercadolivre.com.br/'
produto_name = input('Qual produto você quer ? ')

response = requests.get(url_base + produto_name)

soup = BeautifulSoup(response.text, 'html.parser')

produtos = soup.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default andes-card--animated'})

for produto in produtos:

    titulo = produto.find('h2', attrs={'class', 'ui-search-item__title ui-search-item__group__element'})
    link = produto.find('a', attrs={'class': 'ui-search-link'})
    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

    #print('Título do produto', titulo.text)
    #print('Link do produto: ', link['href'])
    if (centavos):
        ('Preço do produto: R$', real.text + ',' + centavos.text, '\n')
    else:
        ('Preço do produto: R$', real.text, '\n')

    lista = []
    lista.append([titulo, link['href'], real, centavos])
    
    tabela = pd.DataFrame(lista, columns=['Título', 'Link', 'Preço', 'centavos'] )

    print(tabela)