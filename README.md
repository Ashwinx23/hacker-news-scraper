# Hacker News Web Scraper 📰

This Python project scrapes the top headlines from [Hacker News](https://news.ycombinator.com) using BeautifulSoup and Requests.

## Features
- Scrapes news titles and links from the first 3 pages
- Stores the scraped data in a CSV file
- Cleans the text by removing whitespace and strange characters
- Handles errors and request failures gracefully
- Saves both raw and cleaned data

## Files in this Repo
- `hacker_news_scraper.py` — Final working script
- `hacker_news_3pages.csv` — Scraped raw data
- `hacker_news_cleaned.csv` — Cleaned version
- `.gitignore` — To ignore unnecessary files

## Tools Used
- Python 3
- Requests
- BeautifulSoup (bs4)
- Pandas
- Jupyter Notebook


