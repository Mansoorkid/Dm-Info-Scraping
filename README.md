# Instagram DM Analyzer

This project fetches Instagram DMs, calculates the time intervals between messages, and performs sentiment and entity analysis on the messages.

## Setup

1. Install required libraries:
    ```
    pip install -r requirements.txt
    or
    pip install selenium beautifulsoup4
    ```

2. Download the appropriate WebDriver for your browser and ensure it's in your system's PATH.
   ```
   Chrome: ChromeDriver
    Firefox: GeckoDriver
    Edge: EdgeDriver
   ```

4. Run the script:
    ```
    python main.py
    ```
5. Output
   ```
   The scraped data will be stored in the output directory in the format specified in the script.
   ```
Notes
```
This script interacts with Instagram's web interface and may be subject to changes in the website structure, which could break the script. Please keep the libraries and WebDriver up-to-date.
Use this script responsibly and respect Instagram's terms of service.
```
License
```
MIT License
```
