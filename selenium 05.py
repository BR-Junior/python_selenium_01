from cgitb import text
from dataclasses import replace
from attr import attr, attrs
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("window-size=400,800")
#options.add_argument('--headless')

browser = webdriver.Chrome(options=options)

browser.get('https://statusinvest.com.br/')




btn_menu = browser.find_element_by_css_selector('#main-nav-nav > div > div > div > ul > li.nav-item.d-block.d-md-none.p-relative > a > i').click()
btn_avancado = browser.find_element_by_css_selector('#left-menu-initial > ul:nth-child(1) > li:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)').click()
btn_busca = browser.find_element_by_xpath('//*[@id="main-2"]/div[3]/div/div/div/button[2]').click()
time.sleep(2)
btn_10 = browser.find_element_by_css_selector('#list-result > div > div.pagination-control.d-flex.justify-start.align-items-center > div > input').click()
btn_todos = browser.find_element_by_xpath('/html/body/main/div[4]/div/div[2]/div/div[2]/div/ul/li[3]').click()
time.sleep(5)


page_content = browser.page_source
soup = BeautifulSoup(page_content, 'html.parser') # traz o conteudo html da pagina parecido com o soup


tickers = soup.findAll('tr', attrs={'class': 'item'})#.find('span', attrs={'class': 'ticker waves-effect'})

for ticker in tickers:
    nome = ticker.find('span', attrs={'class': 'ticker waves-effect'}).text
    ev_ebit = ticker.find('td', attrs={'data-key': 'eV_Ebit'}).text
    ev_ebit_float = float(ev_ebit.replace(',','.'))
    
    roic = ticker.find('td', attrs={'data-key': 'roic'}).text
    roic_float = float(roic.replace(',','.'))
        
    lista = []
    lista.append([nome, ev_ebit_float + roic_float])
    print(lista)


# print(ticker, ev_ebit, roic)
# ev_ebit_float = float(ev_ebit.replace(',','.'))
# roic_float = float(roic.replace(',','.'))

#print(ev_ebit_float + roic_float)


    

