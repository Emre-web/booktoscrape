import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
book_url = ('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')

response = requests.get(book_url, headers=headers)

print(response.request.headers)