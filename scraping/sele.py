from selenium import webdriver
import time


def get_html(driver, url):
    driver.get(url)
    time.sleep(1)

    table_element = driver.find_element_by_class_name('DataGrid')
    html_content = table_element.get_attribute('outerHTML')

    return html_content


def get_total_page(driver, url):
    driver.get(url)
    time.sleep(1)

    pagination_div = driver.find_element_by_class_name('page')
    html_content = pagination_div.get_attribute('outerHTML')

    return html_content
