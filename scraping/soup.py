from bs4 import BeautifulSoup
import urllib.parse


def get_data_in_tr(tr):
    item_in_tr = []

    for item in tr:
        item_in_tr.append(item)

    ip_address = convert_unquote(tr.script.get_text(strip=True))

    port = try_get_text(item_in_tr[1])
    protocol = try_get_text(item_in_tr[2])
    anonymity = try_get_text(item_in_tr[3])
    country = try_get_text(item_in_tr[4])
    region = try_get_text(item_in_tr[5])
    city = try_get_text(item_in_tr[6])
    uptime = try_get_text(item_in_tr[7]).replace('%', '')

    response = convert_style(item_in_tr[8])
    transfer = convert_style(item_in_tr[9])

    return {
        'ip_address': ip_address,
        'port': port,
        'protocol': protocol,
        'anonymity': anonymity,
        'country': country,
        'region': region,
        'city': city,
        'uptime': float(uptime),
        'response': int(response),
        'transfer': int(transfer)
    }


def try_get_text(item):
    try:
        text = item.get_text(strip=True)
        return text
    except:
        return ''


def convert_unquote(text):
    try:
        bs = BeautifulSoup(urllib.parse.unquote(text), 'html.parser')

        text_convert = bs.a.get_text(strip=True)

        return text_convert
    except:
        return ''


def convert_style(tag):
    try:
        bs = BeautifulSoup(str(tag), 'html.parser')

        text_style = bs.span["style"]

        text = text_style.split(":")[1]

        tag_convert = text.replace('%;background', '').strip()

        return tag_convert
    except:
        return ''


def get_total_number_of_pages(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        total_page = soup.find_all('a')
        return len(total_page)
    except:
        return 0
