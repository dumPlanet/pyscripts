import sqlite3
import random

# connect database
conn = sqlite3.connect('database/workdatabase.sqlite')
cursor = conn.cursor()


# generate random number function
def generate_unique_number():
    return random.randint(10000, 99999)


def generateNumber(sql_select, sql_update, conn, cursor):
    # load selected data from table
    cursor.execute(sql_select)
    rows = cursor.fetchall()

    # loop
    for row in rows:
        author_name = row[0]
        author_surname = row[1]

        # generate a number for ...
        authorID = generate_unique_number()

        # execute update
        cursor.execute(sql_update, (authorID, author_name, author_surname))
        conn.commit()

    # Verbindung zur Datenbank schließen
    conn.close()


# Variables
sql_select = "SELECT author_name, author_surname FROM quotes"
sql_update = "UPDATE quotes SET authorID = ? WHERE author_name = ? AND author_surname = ?"


# Execute Script
generateNumber(sql_select, sql_update, conn, cursor)
