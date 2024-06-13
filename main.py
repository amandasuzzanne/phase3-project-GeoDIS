# main.py
from geodis_db import GeoDISDB
from menus import continent_menu, language_menu, country_menu, city_menu

def main_menu():
    db = GeoDISDB()

    while True:
        print("\nMain Menu:")
        print("1. Continent menu")
        print("2. Language menu")
        print("3. Country menu")
        print("4. City menu")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            continent_menu(db)
        elif choice == '2':
            language_menu(db)
        elif choice == '3':
            country_menu(db)
        elif choice == '4':
            city_menu(db)
        elif choice == '5':
            db.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
