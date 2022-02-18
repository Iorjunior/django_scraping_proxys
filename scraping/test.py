import sele
import model
import soup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


URL_BASE = 'https://www.freeproxylists.net/?page='

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

sele.get_total_page(driver, URL_BASE)
