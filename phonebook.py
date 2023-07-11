class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"Имя: {self.name}\nНомер телефона: {self.phone_number}"


class Phonebook:
    def __init__(self, file_path):
        self.contacts = []
        self.file_path = file_path

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                return True
        return False

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower():
                found_contacts.append(contact)
        return found_contacts

    def display_contacts(self):
        if not self.contacts:
            print("Справочник пуст.")
        else:
            for contact in self.contacts:
                print(contact)

    def edit_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Найден контакт:")
                print(contact)
                new_name = input("Введите новое имя: ")
                new_phone_number = input("Введите новый номер телефона: ")
                contact.name = new_name
                contact.phone_number = new_phone_number
                self.save_contacts()
                # print("Контакт успешно отредактирован.")
                return True
        return False

    def save_contacts(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone_number}\n")

    def load_contacts(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line in file:
                    name, phone_number = line.strip().split(",")
                    contact = Contact(name, phone_number)
                    self.contacts.append(contact)
        except FileNotFoundError:
            pass
