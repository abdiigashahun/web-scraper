import requests
import time
from fake_useragent import UserAgent

ua = UserAgent()

def get_headers():
    return {
        "User-Agent": ua.random,
        "Accept-Language": "en-US,en;q=0.9"
    }

def safe_request(url, proxies=None, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(
                url,
                headers=get_headers(),
                proxies=proxies,
                timeout=10
            )
            response.raise_for_status()
            return response
        except Exception as e:
            print(f"Retry {attempt+1} failed: {e}")
            time.sleep(2)
    return None