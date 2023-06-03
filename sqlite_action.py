import sqlite3
import random

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('database/workdatabase.sqlite')
cursor = conn.cursor()


# Funktion zum Generieren einer eindeutigen zufälligen Nummer
def generate_unique_number():
    return random.randint(10000, 99999)  # Beispielbereich für die zufällige Nummer


# SQL-Statement zum Abrufen der relevanten Datensätze
sql_select = "SELECT author_name, author_surname FROM quotes"

# Datensätze abrufen
cursor.execute(sql_select)
rows = cursor.fetchall()

# Schleife über die abgerufenen Datensätze
for row in rows:
    author_name = row[0]
    author_surname = row[1]

    # Eindeutige Nummer generieren
    authorID = generate_unique_number()

    # SQL-Statement zum Aktualisieren des Datensatzes mit der eindeutigen Nummer
    sql_update = "UPDATE quotes SET authorID = ? WHERE author_name = ? AND author_surname = ?"

    # Datensatz aktualisieren
    cursor.execute(sql_update, (authorID, author_name, author_surname))
    conn.commit()

# Verbindung zur Datenbank schließen
conn.close()
