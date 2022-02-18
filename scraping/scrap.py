
import model
import sele
import soup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

URL_BASE = 'https://www.freeproxylists.net/?page='

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# obtendo o numeros de paginas
print('>>>[Obtendo Total de paginas]')

numbers_of_pages = soup.get_total_number_of_pages(
    sele.get_total_page(driver, URL_BASE))

print(f'>>>[Total de paginas: {numbers_of_pages} ]')

print('>>>[Começando Scraping]')

for page in range(1, numbers_of_pages + 1):
    print(f'>>>[Scraping na pagina: [{page}]')

    all_items = []
    html_content = sele.get_html(driver, f'{URL_BASE}{page}')

    soup_html = BeautifulSoup(html_content, 'html.parser')

    for tr in soup_html.find_all('tr', attrs={'class': 'Odd'}):
        if len(tr) > 6:
            item = soup.get_data_in_tr(tr)
            all_items.append(item)
        else:
            pass

    for tr in soup_html.find_all('tr', attrs={'class': 'Even'}):
        if len(tr) > 6:
            item = soup.get_data_in_tr(tr)
            all_items.append(item)
        else:
            pass

    print(f'>>>[Salvando pagina: [{page}] no banco de dados]')

    model.save_data(all_items)
