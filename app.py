import sqlite3

def create_tables():
    connection = sqlite3.connect("geodis.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS continents(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   area FLOAT,
                   population INTEGER,
                   countries INTEGER 
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS languages(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   language_family TEXT,
                   writing_system TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS countries(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   area FLOAT,
                   population INTEGER,
                   continent_id INTEGER,
                   language_id INTEGER,
                   FOREIGN KEY(continent_id) REFERENCES continents(id),
                   FOREIGN KEY(language_id) REFERENCES languages(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS cities(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   area FLOAT,
                   population INTEGER,
                   country_id INTEGER,
                   FOREIGN KEY(country_id) REFERENCES countries(id)
    )''')

    connection.commit()
    connection.close()

# Create the tables
create_tables()

class GeoDISDB:
    def __init__(self):
        self.connection = sqlite3.connect("geodis.db")
        self.cursor = self.connection.cursor()

    def add_continent(self, name, area, population, countries):
        self.cursor.execute('''INSERT INTO continents(name, area, population, countries) VALUES(?, ?, ?, ?)''', (name, area, population, countries))
        self.connection.commit()

    def add_language(self, name, language_family, writing_system):
        self.cursor.execute('''INSERT INTO languages(name, language_family, writing_system) VALUES(?, ?, ?)''', (name, language_family, writing_system))
        self.connection.commit()

    def add_country(self, name, area, population, continent_id, language_id):
        self.cursor.execute('''INSERT INTO countries(name, area, population, continent_id, language_id) VALUES(?, ?, ?, ?, ?)''', (name, area, population, continent_id, language_id))
        self.connection.commit()

    def add_city(self, name, area, population, country_id):
        self.cursor.execute('''INSERT INTO cities(name, area, population, country_id) VALUES(?, ?, ?, ?)''', (name, area, population, country_id))
        self.connection.commit()

    def update_continent(self, id, name, area, population, countries):
        self.cursor.execute('''UPDATE continents SET name = ?, area = ?, population = ?, countries = ? WHERE id = ?''', (name, area, population, countries, id))
        self.connection.commit()

    def update_language(self, id, name, language_family, writing_system):
        self.cursor.execute('''UPDATE languages SET name = ?, language_family = ?, writing_system = ? WHERE id = ?''', (name, language_family, writing_system, id))
        self.connection.commit()

    def update_country(self, id, name, area, population, continent_id, language_id):
        self.cursor.execute('''UPDATE countries SET name = ?, area = ?, population = ?, continent_id = ?, language_id = ? WHERE id = ?''', (name, area, population, continent_id, language_id, id))
        self.connection.commit()

    def update_city(self, id, name, area, population, country_id):
        self.cursor.execute('''UPDATE cities SET name = ?, area = ?, population = ?, country_id = ? WHERE id = ?''', (name, area, population, country_id, id))
        self.connection.commit()

    def delete_continent(self, id):
        self.cursor.execute('''DELETE FROM continents WHERE id = ?''', (id,))
        self.connection.commit()

    def delete_language(self, id):
        self.cursor.execute('''DELETE FROM languages WHERE id = ?''', (id,))
        self.connection.commit()

    def delete_country(self, id):
        self.cursor.execute('''DELETE FROM countries WHERE id = ?''', (id,))
        self.connection.commit()

    def delete_city(self, id):
        self.cursor.execute('''DELETE FROM cities WHERE id = ?''', (id,))
        self.connection.commit()

    def list_continents(self):
        self.cursor.execute('''SELECT * FROM continents''')
        continents = self.cursor.fetchall()
        return continents

    def list_languages(self):
        self.cursor.execute('''SELECT * FROM languages''')
        languages = self.cursor.fetchall()
        return languages

    def list_countries(self):
        self.cursor.execute('''
            SELECT countries.id, countries.name, countries.area, countries.population, 
                   continents.name AS continent_name, languages.name AS language_name
            FROM countries 
            LEFT JOIN continents ON countries.continent_id = continents.id
            LEFT JOIN languages ON countries.language_id = languages.id
        ''')
        countries = self.cursor.fetchall()
        return countries

    def list_cities(self): 
        self.cursor.execute('''
            SELECT cities.id, cities.name, cities.area, cities.population, countries.name AS country_name
            FROM cities
            LEFT JOIN countries ON cities.country_id = countries.id
        ''')
        cities = self.cursor.fetchall()
        return cities

    def close(self):
        self.connection.close()


# Continent menu
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
            
            name = input("Enter continent name: ")
            area = input("Enter continent area: ")
            population = input("Enter continent population: ")
            countries = input("Enter number of countries in continent: ")
            db.add_continent(name, area, population, countries)
        elif choice == '2':
            continents = db.list_continents()
            for continent in continents:
                print(f'Continent ID: {continent[0]}, Name: {continent[1]}, Area: {continent[2]}, Population: {continent[3]}, Countries: {continent[4]}')
        elif choice == '3':
            print("\nThese are the continents you can update:")
            continents = db.list_continents()
            for continent in continents:
                print(f'Continent ID: {continent[0]}, Name: {continent[1]}, Area: {continent[2]}, Population: {continent[3]}, Countries: {continent[4]}')

            id = input("Enter continent ID to update: ")
            name = input("Enter new continent name: ")
            area = input("Enter new continent area: ")
            population = input("Enter new continent population: ")
            countries = input("Enter new number of countries in continent: ")
            db.update_continent(id, name, area, population, countries)
        elif choice == '4':
            print("\nThese are the continents you can delete:")
            continents = db.list_continents()
            for continent in continents:
                print(f'Continent ID: {continent[0]}, Name: {continent[1]}')

            id = input("Enter continent ID to delete: ")
            db.delete_continent(id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

# Language menu
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

            name = input("Enter language name: ")
            language_family = input("Enter language family: ")
            writing_system = input("Enter language writing system: ")
            db.add_language(name, language_family, writing_system)
        elif choice == '2':
            languages = db.list_languages()
            for language in languages:
                print(f'Language ID: {language[0]}, Name: {language[1]}, Language Family: {language[2]}, Writing System: {language[3]}')
        elif choice == '3':
            print("\nThese are the languages you can update:")
            languages = db.list_languages()
            for language in languages:
                print(f'Language ID: {language[0]}, Name: {language[1]}, Language Family: {language[2]}, Writing System: {language[3]}')

            id = input("Enter language ID to update: ")
            name = input("Enter new language name: ")
            language_family = input("Enter new language family: ")
            writing_system = input("Enter new writing system: ")
            db.update_language(id, name, language_family, writing_system)
        elif choice == '4':
            print("\nThese are languages you can delete:")
            languages = db.list_languages()
            for language in languages:
                print(f'Language ID: {language[0]}, Name: {language[1]}')

            id = input("Enter language ID to delete: ")
            db.delete_language(id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

# Country menu
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
            area = input("Enter country area: ")
            population = input("Enter country population: ")
            continent_id = input("Enter continent ID: ")
            language_id = input("Enter language ID: ")
            db.add_country(name, area, population, continent_id, language_id)
        elif choice == '2':
            countries = db.list_countries()
            for country in countries:
                print(f'Country ID: {country[0]}, Name: {country[1]}, Area: {country[2]}, Population: {country[3]}, Continent: {country[4]}, Language: {country[5]}')
        elif choice == '3':
            print("\nThese are the countries you can updaet:")
            countries = db.list_countries()
            for country in countries:
                print(f'Country ID: {country[0]}, Name: {country[1]}, Area: {country[2]}, Population: {country[3]}, Continent: {country[4]}, Language: {country[5]}')

            id = input("Enter country ID to update: ")
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

            id = input("Enter country ID to delete: ")
            db.delete_country(id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

# City menu
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
            
            name = input("Enter city name: ")
            area = input("Enter city area: ")
            population = input("Enter city population: ")
            country_id = input("Enter country ID: ")
            db.add_city(name, area, population, country_id)
        elif choice == '2':
            cities = db.list_cities()
            for city in cities:
                print(f'City ID: {city[0]}, Name: {city[1]}, Area: {city[2]}, Population: {city[3]}, Country: {city[4]}')
        elif choice == '3':
            print("These are the cities you can update:")
            cities = db.list_cities()
            for city in cities:
                print(f'City ID: {city[0]}, Name: {city[1]}, Area: {city[2]}, Population: {city[3]}, Country: {city[4]}')

            id = input("Enter city ID to update: ")
            name = input("Enter new city name: ")
            area = input("Enter new city area: ")
            population = input("Enter new city population: ")
            country_id = input("Enter new country ID: ")
            db.update_city(id, name, area, population, country_id)
        elif choice == '4':
            print("These are the cities you can delete:")
            cities = db.list_cities()
            for city in cities:
                print(f'City ID: {city[0]}, Name: {city[1]}')

            id = input("Enter city ID to delete: ")
            db.delete_city(id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

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
