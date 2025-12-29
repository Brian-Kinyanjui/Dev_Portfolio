import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)

# 1. Turn the website code into a "Soup" object
soup = BeautifulSoup(response.text, "html.parser")

# 2. Get the Whole Shelf (The List)
all_books = soup.find_all("h3")

# 3. Loop through the list one by one
for book in all_books:
    # "book" is the single item. We can read its text.
    print(book.text)