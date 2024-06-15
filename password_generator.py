import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_and_display_password():
    length = int(length_entry.get())
    password = generate_password(length)
    password_display.config(text="Generated Password: " + password)

def reset_password():
    length_entry.delete(0, tk.END)
    password_display.config(text="")


root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Enter Length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
reset_button = tk.Button(root, text="Reset", command=reset_password)
password_display = tk.Label(root, text="")


length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, column=0, padx=10, pady=10)
reset_button.grid(row=1, column=1, padx=10, pady=10)
password_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
 
