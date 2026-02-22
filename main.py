from scraper import get_listing, extract_product_links, scrape_product
import time

def main():
    all_data = []

    for page in range(1, 4):
        soup = get_listing(page)
        if not soup:
            continue

        links = extract_product_links(soup)

        for link in links:
            try:
                data = scrape_product(link)
                if data:
                    all_data.append(data)
                time.sleep(1)
            except Exception as e:
                print("Error scraping product:", e)

    print(all_data)

if __name__ == "__main__":
    main()