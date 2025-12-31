import requests
import tkinter as tk  # This is the GUI library

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    
    try:
        # 1. Ask the internet for data
        response = requests.get(url)
        
        # 2. Check if the internet replied successfully
        response.raise_for_status() 
        
        # 3. Dig for the gold
        data = response.json()
        price = data["bpi"]["USD"]["rate"]
        
        # 4. Update the screen
        # We use 'config' for standard tkinter, 'configure' is also fine
        price_label.config(text=f"${price}") 
        print(f"Success! Price: ${price}")
        
    except Exception as e:
        price_label.config(text="Error!")
        print(f"❌ THE ERROR IS: {e}")

# --- THE MISSING PIECES BELOW ---

# 1. Create the Window
root = tk.Tk()
root.title("Crypto App")
root.geometry("400x200")

# 2. Create the Label (price_label)
# This must exist BEFORE we try to change its text in the function
price_label = tk.Label(root, text="Press the button...", font=("Arial", 20))
price_label.pack(pady=20)

# 3. Create a Button to trigger the function
refresh_btn = tk.Button(root, text="Get Price", command=get_bitcoin_price)
refresh_btn.pack()

# 4. Start the App
root.mainloop()