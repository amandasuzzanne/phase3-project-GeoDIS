# Module for the menus used for user interaction
from geodis_db import GeoDISDB

def continent_menu(db):
    while True:
        print("\nContinent Menu:")
        print("1. Add continent")
        print("2. List continents")
        print("3. Update continent")
        print("4. Delete continent")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nThese continents have already been added:")
            continents = db.list_continents()
            for continent in continents:
                print(f'Continent ID: {continent[0]}, Name: {continent[1]}')
            
            name = input("\nEnter continent name: ")
            area = input("Enter continent area (in sqkm): ")
            population = input("Enter continent population: ")
            countries = input("Enter number of countries in continent: ")
            db.add_continent(name, area, population, countries)
        elif choice == '2':
            print("\nHere is a list of all the continents:")
            continents = db.list_continents()
            for continent in continents:
                print(f'Continent ID: {continent[0]}, Name: {continent[1]}, Area (in sqkm): {continent[2]}, Population: {continent[3]}, Countries: {continent[4]}')
        elif choice == '3':
            print("\nThese are the continents you can update:")
            continents = db.list_continents()
            for continent in continents:
                print(f'Continent ID: {continent[0]}, Name: {continent[1]}, Area (in sqkm): {continent[2]}, Population: {continent[3]}, Countries: {continent[4]}')

            id = input("/nEnter continent ID to update: ")
            name = input("Enter new continent name: ")
            area = input("Enter new continent area (in sqkm): ")
            population = input("Enter new continent population: ")
            countries = input("Enter new number of countries in continent: ")
            db.update_continent(id, name, area, population, countries)
        elif choice == '4':
            print("\nThese are the continents you can delete:")
            continents = db.list_continents()
            for continent in continents:
                print(f'Continent ID: {continent[0]}, Name: {continent[1]}')

            id = input("\nEnter continent ID to delete: ")
            db.delete_continent(id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

def language_menu(db):
    while True:
        print("\nLanguage Menu:")
        print("1. Add language")
        print("2. List languages")
        print("3. Update language")
        print("4. Delete language")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nThese languages have already been added:")
            languages = db.list_languages()
            for language in languages:
                print(f'Language ID: {language[0]}, Name: {language[1]}, Language Family: {language[2]}, Writing System: {language[3]}')

            name = input("/nEnter language name: ")
            language_family = input("Enter language family: ")
            writing_system = input("Enter language writing system: ")
            db.add_language(name, language_family, writing_system)
        elif choice == '2':
            print("\nHere is a list of all the languages:")
            languages = db.list_languages()
            for language in languages:
                print(f'Language ID: {language[0]}, Name: {language[1]}, Language Family: {language[2]}, Writing System: {language[3]}')
        elif choice == '3':
            print("\nThese are the languages you can update:")
            languages = db.list_languages()
            for language in languages:
                print(f'Language ID: {language[0]}, Name: {language[1]}, Language Family: {language[2]}, Writing System: {language[3]}')

            id = input("/nEnter language ID to update: ")
            name = input("Enter new language name: ")
            language_family = input("Enter new language family: ")
            writing_system = input("Enter new writing system: ")
            db.update_language(id, name, language_family, writing_system)
        elif choice == '4':
            print("\nThese are the languages you can delete:")
            languages = db.list_languages()
            for language in languages:
                print(f'Language ID: {language[0]}, Name: {language[1]}')

            id = input("/nEnter language ID to delete: ")
            db.delete_language(id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

def country_menu(db):
    while True:
        print("\nCountry Menu:")
        print("1. Add country")
        print("2. List countries")
        print("3. Update country")
        print("4. Delete country")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("/nThese countries have already been added:")
            countries = db.list_countries()
            for country in countries:
                print(f'Country ID: {country[0]}, Name: {country[1]}')

            print("\nThese are the continents you can select from:")
            continents = db.list_continents()
            for continent in continents:
                print(f'Continent ID: {continent[0]}, Name: {continent[1]}')

            print("\nThese are the languages you can select from:")
            languages = db.list_languages()
            for language in languages:
                print(f'Language ID: {language[0]}, Name: {language[1]}')
            name = input("\nEnter country name: ")
            area = input("Enter country area (in sqkm): ")
            population = input("Enter country population: ")
            continent_id = input("Enter continent ID: ")
            language_id = input("Enter language ID: ")
            db.add_country(name, area, population, continent_id, language_id)
        elif choice == '2':
            print("\nHere is a list of all the countries:")
            countries = db.list_countries()
            for country in countries:
                print(f'Country ID: {country[0]}, Name: {country[1]}, Area (in sqkm): {country[2]}, Population: {country[3]}, Continent: {country[4]}, Language: {country[5]}')
        elif choice == '3':
            print("\nThese are the countries you can updaet:")
            countries = db.list_countries()
            for country in countries:
                print(f'Country ID: {country[0]}, Name: {country[1]}, Area (in sqkm): {country[2]}, Population: {country[3]}, Continent: {country[4]}, Language: {country[5]}')

            id = input("\nEnter country ID to update: ")
            name = input("Enter new country name: ")
            area = input("Enter new country area: ")
            population = input("Enter new country population: ")
            continent_id = input("Enter new continent ID: ")
            language_id = input("Enter new language ID: ")
            db.update_country(id, name, area, population, continent_id, language_id)
        elif choice == '4':
            print("\nThese are the countries you can delete:")
            countries = db.list_countries()
            for country in countries:
                print(f'Country ID: {country[0]}, Name: {country[1]}')

            id = input("\nEnter country ID to delete: ")
            db.delete_country(id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

def city_menu(db):
    while True:
        print("\nCity Menu:")
        print("1. Add city")
        print("2. List cities")
        print("3. Update city")
        print("4. Delete city")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nThese cities have already been added:")
            cities = db.list_cities()
            for city in cities:
                print(f'City ID: {city[0]}, Name: {city[1]}')

            print("\nThese are the countries you can select from:")
            countries = db.list_countries()
            for country in countries:
                print(f'Country ID: {country[0]}, Name: {country[1]}')
            
            name = input("\nEnter city name: ")
            area = input("Enter city area (in sqkm): ")
            population = input("Enter city population: ")
            country_id = input("Enter country ID: ")
            db.add_city(name, area, population, country_id)
        elif choice == '2':
            print("\nHere is a list of all the cities:")
            cities = db.list_cities()
            for city in cities:
                print(f'City ID: {city[0]}, Name: {city[1]}, Area (in sqkm): {city[2]}, Population: {city[3]}, Country: {city[4]}')
        elif choice == '3':
            print("\nThese are the cities you can update:")
            cities = db.list_cities()
            for city in cities:
                print(f'City ID: {city[0]}, Name: {city[1]}, Area (in sqkm): {city[2]}, Population: {city[3]}, Country: {city[4]}')

            id = input("\nEnter city ID to update: ")
            name = input("Enter city name: ")
            area = input("Enter city area (in sqkm): ")
            population = input("Enter city population: ")
            country_id = input("Enter country ID: ")
            db.update_city(id, name, area, population, country_id)
        elif choice == '4':
            print("\nThese are the cities you can delete:")
            cities = db.list_cities()
            for city in cities:
                print(f'City ID: {city[0]}, Name: {city[1]}')

            id = input("\nEnter city ID to delete: ")
            db.delete_city(id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")
