import json
import tkinter as tk
from tkinter import messagebox

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact():
    global contacts, name_entry, phone_entry, email_entry
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        messagebox.showinfo("Success", f"{name} added to contacts.")
        clear_entries()
        update_contact_list()
    else:
        messagebox.showwarning("Error", "Please fill in all fields.")

def view_contacts():
    global contacts, contact_listbox
    contact_listbox.delete(0, tk.END)
    if not contacts:
        contact_listbox.insert(tk.END, "No contacts available.")
    else:
        for name, info in contacts.items():
            contact_listbox.insert(tk.END, name)

def edit_contact():
    global contacts, name_entry, phone_entry, email_entry, contact_listbox

    selected_contact = contact_listbox.curselection()
    if selected_contact:
        selected_contact = selected_contact[0]
        name = contact_listbox.get(selected_contact)

        new_phone = phone_entry.get()
        new_email = email_entry.get()

        if new_phone and new_email:
            contacts[name]["phone"] = new_phone
            contacts[name]["email"] = new_email
            save_contacts(contacts)
            messagebox.showinfo("Success", f"{name}'s information updated.")
            clear_entries()
            update_contact_list()
        else:
            messagebox.showwarning("Error", "Please fill in all fields.")
    else:
        messagebox.showwarning("Error", "Please select a contact to edit.")

def delete_contact():
    global contacts, contact_listbox

    selected_contact = contact_listbox.curselection()
    if selected_contact:
        selected_contact = selected_contact[0]
        name = contact_listbox.get(selected_contact)

        response = messagebox.askyesno("Confirmation", f"Do you want to delete {name} from contacts?")
        if response == tk.YES:
            del contacts[name]
            save_contacts(contacts)
            messagebox.showinfo("Success", f"{name} deleted from contacts.")
            update_contact_list()
            clear_entries()
    else:
        messagebox.showwarning("Error", "Please select a contact to delete.")

def clear_entries():
    global name_entry, phone_entry, email_entry
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def update_contact_list():
    global contacts, contact_listbox
    view_contacts()
    contact_listbox.selection_clear(0, tk.END)

def load_contact_details(event):
    global contacts, name_entry, phone_entry, email_entry, contact_listbox

    selected_contact = contact_listbox.curselection()
    if selected_contact:
        selected_contact = selected_contact[0]
        name = contact_listbox.get(selected_contact)

        name_entry.delete(0, tk.END)
        name_entry.insert(tk.END, name)

        phone_entry.delete(0, tk.END)
        phone_entry.insert(tk.END, contacts[name]["phone"])

        email_entry.delete(0, tk.END)
        email_entry.insert(tk.END, contacts[name]["email"])

def main():
    global contacts, name_entry, phone_entry, email_entry, contact_listbox
    contacts = load_contacts()

    window = tk.Tk()
    window.title("Contact Management")
    window.geometry("600x400")  # Set window size

    # Add a title label
    title_label = tk.Label(window, text="Contact Management", font=("Helvetica", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=3, pady=10)

    # Entry fields
    name_label = tk.Label(window, text="Name:")
    name_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    name_entry = tk.Entry(window)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    phone_label = tk.Label(window, text="Phone:")
    phone_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    phone_entry = tk.Entry(window)
    phone_entry.grid(row=2, column=1, padx=10, pady=5)

    email_label = tk.Label(window, text="Email:")
    email_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    email_entry = tk.Entry(window)
    email_entry.grid(row=3, column=1, padx=10, pady=5)

    # Buttons
    add_button = tk.Button(window, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white")
    add_button.grid(row=4, column=0, columnspan=2, pady=10)

    edit_button = tk.Button(window, text="Edit Contact", command=edit_contact, bg="#008CBA", fg="white")
    edit_button.grid(row=5, column=0, columnspan=2, pady=5)

    delete_button = tk.Button(window, text="Delete Contact", command=delete_contact, bg="#FF0000", fg="white")
    delete_button.grid(row=6, column=0, columnspan=2, pady=5)

    # Contact List
    contact_listbox = tk.Listbox(window, width=25, height=15)
    contact_listbox.grid(row=1, column=2, rowspan=6, padx=10, pady=5, sticky=tk.W)

    # Load existing contacts
    update_contact_list()

    # Bind the event to load contact details when clicking on a contact in the listbox
    contact_listbox.bind("<<ListboxSelect>>", load_contact_details)

    # Center the window on the screen
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x_coordinate = (window.winfo_screenwidth() - width) // 2
    y_coordinate = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

    window.mainloop()

if __name__ == "__main__":
    main()
