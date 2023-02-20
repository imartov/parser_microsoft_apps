import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


def get_content(url):
    resp = requests.get(url)
    with open('apps.html', 'w') as f:
        f.write(resp.text)


def parse_content():
    url = "https://apps.microsoft.com/store/category/Business"
    get_content(url)

if __name__ == '__main__':
    parse_content()