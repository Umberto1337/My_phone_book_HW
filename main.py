from phonebook import Contact, Phonebook

def run_phonebook():
    file_path = "phonebook.txt"
    phonebook = Phonebook(file_path)
    phonebook.load_contacts()

    while True:
        print("\nМеню справочника:")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Найти контакт")
        print("4. Вывести все контакты")
        print("5. Редактировать контакт")
        print("6. Выход")

        choice = input("Введите ваш выбор (1-6): ")

        if choice == "1":
            name = input("Введите имя: ")
            phone_number = input("Введите номер телефона: ")
            contact = Contact(name, phone_number)
            phonebook.add_contact(contact)
            print("Контакт добавлен.")
        elif choice == "2":
            name = input("Введите имя: ")
            if phonebook.delete_contact(name):
                print("Контакт удален.")
            else:
                print("Контакт не найден.")
        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска: ")
            found_contacts = phonebook.search_contact(keyword)
            if found_contacts:
                print("Найденные контакты:")
                for contact in found_contacts:
                    print(contact)
            else:
                print("Контакты не найдены.")
        elif choice == "4":
            phonebook.display_contacts()
        elif choice == "5":
            name = input("Введите имя контакта для редактирования: ")
            if phonebook.edit_contact(name):
                print("Контакт успешно отредактирован.")
            else:
                print("Контакт не найден.")
        elif choice == "6":
            break
        else:
            print("Неправильный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    run_phonebook()
