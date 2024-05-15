import re
import tkinter as tk
from tkinter import messagebox

# Function to extract IoCs
def extract_iocs(text):
    ip_regex = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    domain_regex = r'\b(?:[a-z][a-z0-9-]{0,61}[a-z0-9]\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]\b'
    md5_regex = r'\b([a-fA-F\d]{32})\b'
    sha1_regex = r'\b([a-fA-F\d]{40})\b'
    sha256_regex = r'\b([a-fA-F\d]{64})\b'
    
    ip_addresses = re.findall(ip_regex, text)
    urls = re.findall(url_regex, text)
    domains = re.findall(domain_regex, text)
    md5_hashes = re.findall(md5_regex, text)
    sha1_hashes = re.findall(sha1_regex, text)
    sha256_hashes = re.findall(sha256_regex, text)
    
    return ip_addresses, urls, domains, md5_hashes, sha1_hashes, sha256_hashes

# Function to be called when the button is clicked
def button_click():
    text = text_entry.get("1.0", tk.END)
    ip_addresses, urls, domains, md5_hashes, sha1_hashes, sha256_hashes = extract_iocs(text)
    result = "IP Addresses: " + ", ".join(ip_addresses)
    result += "\nURLs: " + ", ".join(urls)
    result += "\nDomains: " + ", ".join(domains)
    result += "\nMD5 Hashes: " + ", ".join(md5_hashes)
    result += "\nSHA-1 Hashes: " + ", ".join(sha1_hashes)
    result += "\nSHA-256 Hashes: " + ", ".join(sha256_hashes)
    messagebox.showinfo("Result", result)

# Create the main window
root = tk.Tk()

# Set the title
root.title("IoC Vacuum")

# Create a label
prompt_label = tk.Label(root, text="Please copy text into box")
prompt_label.pack()


# Create a text entry widget
text_entry = tk.Text(root, width=50, height=10)
text_entry.pack()

# Create a button
# Create a button with a star symbol
button = tk.Button(root, text="\u2605 Extract IoCs \u2605", command=button_click, fg="black", bg="red")
button.pack()

# Start the main loop
root.mainloop()
