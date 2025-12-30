import requests
import csv  # <--- NEW TOOL: Lets us work with Excel files
from bs4 import BeautifulSoup

# 1. Connect to the website
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 2. Open a new Excel file (CSV) in "write mode" ('w')
#    newline='' prevents empty lines between rows
#    encoding='utf-8' handles special characters (like currency symbols)
file = open('books.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(file)

# 3. Create the Header Row (The titles at the top of the column)
writer.writerow(['Book Title'])

# 4. Find the books and write them to the file
all_books = soup.find_all("h3")

for book in all_books:
    title = book.text
    # Write the title into the file
    writer.writerow([title])
    print(f"Saved: {title}") # Just so we can see it working in the terminal

# 5. Close the file (Important! Saves the data)
file.close()
print("Scraping Complete. Check books.csv! 🚀")