import customtkinter

# 1. Start the App
app = customtkinter.CTk()
app.geometry("600x500")
app.title("My First App")
my_entry = customtkinter.CTkEntry(app, placeholder_text="Type something...")
my_entry.pack(pady=10)

# --- THE LOGIC (Backend) ---
def button_event():
    password = my_entry.get()
    
    if password == "1234":
        title.configure(text="Access Granted! ✅", text_color="green")
    else:
        title.configure(text="Access Denied! ❌", text_color="red")

# --- THE VISUALS (Frontend) ---

# 2. Add the Text
title = customtkinter.CTkLabel(app, text="Hello, Engineer!")
title.pack(pady=20)

# 3. Add the Button (Fixed!)
button = customtkinter.CTkButton(app, text="Click Me", command=button_event)
button.pack(pady=10)


# 4. Keep it Alive
app.mainloop()

