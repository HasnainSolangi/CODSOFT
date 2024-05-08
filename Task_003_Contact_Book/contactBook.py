# Task_003 - Contact Book

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []  # Initialize an empty list to store contacts

    def add_contact(self, contact):
        self.contacts.append(contact)  # Append the new contact to the contacts list

    def view_contact_list(self):
        if not self.contacts:  # Check if the contact list is empty
            print("Contact list is empty.")
        else:
            for i, contact in enumerate(self.contacts, start=1):  # Enumerate through contacts list
                # Print each contact's details including name, phone number, email, and address
                print(f"{i}. Name: {contact.name}")
                print(f"   Phone Number: {contact.phone_number}")
                print(f"   Email: {contact.email}")
                print(f"   Address: {contact.address}")

    def search_contact(self, search_query):
        found_contacts = []  # Initialize an empty list to store found contacts
        for contact in self.contacts:
            # Check if the search query matches contact name or phone number
            if search_query.lower() in contact.name.lower() or search_query in contact.phone_number:
                found_contacts.append(contact)  # Append the found contact to the list
        return found_contacts  # Return the list of found contacts

    def update_contact(self, old_contact, new_contact):
        index = self.contacts.index(old_contact)  # Find the index of the old contact
        self.contacts[index] = new_contact  # Replace old contact with new contact

    def delete_contact(self, contact):
        self.contacts.remove(contact)  # Remove the specified contact from the contacts list

def main():
    contact_book = ContactBook()  # Create an instance of ContactBook
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")  # Prompt user for choice

        if choice == '1':
            # Prompt user to enter contact details and add the contact
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == '2':
            contact_book.view_contact_list()  # View the list of contacts

        elif choice == '3':
            search_query = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_query)
            if found_contacts:
                # Display search results if contacts are found
                print("Search results:")
                for contact in found_contacts:
                    print(f"{contact.name} - {contact.phone_number}")
            else:
                print("No contacts found.")

        elif choice == '4':
            # Update contact details
            search_query = input("Enter name or phone number of contact to update: ")
            found_contacts = contact_book.search_contact(search_query)
            if found_contacts:
                contact_to_update = found_contacts[0]
                name = input("Enter new name (press enter to keep current): ")
                phone_number = input("Enter new phone number (press enter to keep current): ")
                email = input("Enter new email (press enter to keep current): ")
                address = input("Enter new address (press enter to keep current): ")
                new_contact = Contact(name or contact_to_update.name,
                                      phone_number or contact_to_update.phone_number,
                                      email or contact_to_update.email,
                                      address or contact_to_update.address)
                contact_book.update_contact(contact_to_update, new_contact)
                print("Contact updated successfully.")
            else:
                print("Contact not found.")

        elif choice == '5':
            # Delete a contact
            search_query = input("Enter name or phone number of contact to delete: ")
            found_contacts = contact_book.search_contact(search_query)
            if found_contacts:
                contact_book.delete_contact(found_contacts[0])
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")

        elif choice == '6':
            # Exit the program
            print("Thank you for using the Contact Book!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
