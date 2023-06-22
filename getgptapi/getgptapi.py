import requests
from bs4 import BeautifulSoup
import json
from datetime import date

url = "https://docs.getgptapi.com/blog/0x03-free-api-key"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
}

try:
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
    exit(1)

html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

list_items = soup.find_all('li', class_='nx-my-2')

content_list = [item.get_text(strip=True) for item in list_items]

content_list = content_list[9:]

data = {
    'date': str(date.today()),
    'content': content_list
}

filename = 'data.json'
try:
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"The crawled content has been saved to file: {filename}")
except IOError as e:
    print("An error occurred while writing the file:", e)