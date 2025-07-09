import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_hacker_news(pages=3, delay=1, output_file='hacker_news_3pages.csv'):
    base_url = "https://news.ycombinator.com/"
    current_url = base_url
    all_headlines = []

    for page in range(pages):
        try:
            print(f"Scraping page {page + 1}...")
            response = requests.get(current_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')

            headlines = soup.find_all('span', class_='titleline')
            all_headlines.extend(headlines)

            more_link = soup.find('a', string='More')
            if more_link:
                current_url = base_url + more_link['href']
                time.sleep(delay)
            else:
                break

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            break

    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['S.No', 'Title', 'Link'])

        for i, headline in enumerate(all_headlines, start=1):
            link_tag = headline.find('a')
            if link_tag:
                title = link_tag.text.strip()
                link = link_tag['href']
                writer.writerow([i, title, link])

    print(f"Scraping complete. Data saved to: {output_file}")

if __name__ == '__main__':
    scrape_hacker_news()
