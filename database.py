# Database connection and table creation
import sqlite3

def get_db_connection():
    connection = sqlite3.connect("geodis.db")
    return connection

def create_tables():
    connection = get_db_connection()
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
