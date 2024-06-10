# main.py

from scraping import scrape_instagram_dm
from storage import save_to_csv
import config

def main():
    # Scrape Instagram DMs
    dm_data = scrape_instagram_dm(config.USERNAME, config.PASSWORD)
    
    # Save scraped data to CSV
    save_to_csv(dm_data, 'output/dm_data.csv')

if __name__ == "__main__":
    main()
