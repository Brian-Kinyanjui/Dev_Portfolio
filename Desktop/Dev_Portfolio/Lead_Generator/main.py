# Write the Header row (Now with 2 columns)
    writer.writerow(["Book Title", "Price"])
    
    # Loop through the books (We need to find the 'article' container first for better accuracy)
    # This finds the box that holds BOTH title and price
    all_books = soup.find_all("article", class_="product_pod")
    
    for book in all_books:
        # 1. Get the Title (It's inside an 'h3' tag, inside an 'a' tag)
        title = book.h3.a["title"]
        
        # 2. Get the Price (It's inside a 'p' tag with class 'price_color')
        price = book.find("p", class_="price_color").text
        
        # 3. Save both to the file
        writer.writerow([title, price])
        print(f"Saved: {title} - {price}")
