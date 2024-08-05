import tkinter as tk
from tkinter import messagebox

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    
    if name and phone and email:
        contact_list.append((name, phone, email))
        update_contact_listbox()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Please enter name, phone number, and email.")

# Function to update the contact listbox
def update_contact_listbox():
    contacts_lb.delete(0, tk.END)
    for contact in contact_list:
        contacts_lb.insert(tk.END, contact[0])

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Function to display selected contact details
def display_contact(event):
    index = contacts_lb.curselection()[0]
    contact = contact_list[index]
    name_entry.delete(0, tk.END)
    name_entry.insert(tk.END, contact[0])
    phone_entry.delete(0, tk.END)
    phone_entry.insert(tk.END, contact[1])
    email_entry.delete(0, tk.END)
    email_entry.insert(tk.END, contact[2])

# Function to delete selected contact
def delete_contact():
    try:
        index = contacts_lb.curselection()[0]
        contact_list.pop(index)
        update_contact_listbox()
        clear_entries()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a contact to delete.")

# Create main window
root = tk.Tk()
root.title("Contact Manager")

# Contact list
contact_list = []

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

# Entry fields
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Contact listbox
contacts_lb = tk.Listbox(root, width=40)
contacts_lb.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
contacts_lb.bind("<<ListboxSelect>>", display_contact)

# Buttons
add_btn = tk.Button(root, text="Add Contact", command=add_contact)
add_btn.grid(row=4, column=0, padx=10, pady=5)
delete_btn = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_btn.grid(row=4, column=1, padx=10, pady=5)

# Start the GUI
root.mainloop() 