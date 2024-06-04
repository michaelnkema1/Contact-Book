import json

# Function to load contacts from a file
def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

# Function to save contacts to a file
def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added.")

# Function to view all contacts
def view_contacts(contacts):
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts available.")

# Function to search for a contact
def search_contact(contacts):
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

# Function to edit a contact
def edit_contact(contacts):
    name = input("Enter contact name to edit: ")
    if name in contacts:
        print("Current Details:")
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        contacts[name]["phone"] = input("Enter new phone number: ")
        contacts[name]["email"] = input("Enter new email: ")
        print("Contact details updated.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

# Main function
def main():
    filename = "contacts.json"
    contacts = load_contacts(filename)

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(filename, contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
