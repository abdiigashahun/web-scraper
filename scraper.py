from bs4 import BeautifulSoup
from utils import safe_request
from proxy import get_proxy

BASE_URL = "https://example.com/products?page={}"

def get_listing(page):
    url = BASE_URL.format(page)
    response = safe_request(url)
    if not response:
        return None
    return BeautifulSoup(response.text, "html.parser")

def extract_product_links(soup):
    links = []
    for a in soup.select(".product-link"):
        links.append(a["href"])
    return links

def scrape_product(url):
    response = safe_request(url)
    if not response:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    return {
        "title": soup.select_one(".title").text.strip(),
        "price": soup.select_one(".price").text.strip()
    }