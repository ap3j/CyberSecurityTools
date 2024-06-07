import tkinter as tk
from tkinter import messagebox

# Dictionary to store passwords
passwords = {}

# Function to store a password
def store_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website in passwords:
        messagebox.showerror("Error", "Password for this website already stored.")
    else:
        passwords[website] = (username, password)
        messagebox.showinfo("Success", "Password stored successfully.")

# Function to retrieve a password
def retrieve_password():
    website = website_entry.get()

    if website in passwords:
        username, password = passwords[website]
        messagebox.showinfo("Password", f"Username: {username}\nPassword: {password}")
    else:
        messagebox.showerror("Error", "No password stored for this website.")

# Create the main window
root = tk.Tk()

# Create the entry fields
website_entry = tk.Entry(root)
website_entry.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_entry = tk.Entry(root)
password_entry.pack()

# Create the buttons
store_button = tk.Button(root, text="Store Password", command=store_password)
store_button.pack()

retrieve_button = tk.Button(root, text="Retrieve Password", command=retrieve_password)
retrieve_button.pack()

# Start the main loop
root.mainloop()