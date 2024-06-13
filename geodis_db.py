# geodis_db.py
from database import get_db_connection

class GeoDISDB:
    def __init__(self):
        self.connection = get_db_connection()
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
