# Instagram DM Analyzer

This project fetches Instagram DMs, calculates the time intervals between messages, and performs sentiment and entity analysis on the messages.

## Setup

1. Install required libraries:
    ```
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```

2. Set up Instagram API access and get your `client_id`, `client_secret`, `redirect_uri`, and `authorization_code`.

3. Run the script:
    ```
    python main.py
    ```

## Files

- `main.py`: The main script to run the project.
- `fetch_messages.py`: Contains functions to fetch messages from Instagram.
- `analyze_messages.py`: Contains functions to analyze the messages.
