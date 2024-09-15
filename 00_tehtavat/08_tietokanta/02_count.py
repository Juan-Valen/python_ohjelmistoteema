# IDEA
# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin. 
    # Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.


import os
from random import randint
import mysql.connector


def countries_airports_by_type():
    iso_country: str = None
    while not iso_country:
        # INPUT
        os.system("cls")
        iso_country = input("Anna maakoodin (esim. FI): ")
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='dbuser',
        password='sAL_a3ana',
        autocommit=True,
        collation='utf8mb4_general_ci'
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT type, COUNT(ident) FROM airport WHERE iso_country = '{iso_country}' GROUP BY type;")
    result = cursor.fetchall()
    for row in result:
        print(row)
# INTRO
os.system("cls")
# LOGIC

countries_airports_by_type()
# result = cursor.fetchall
# result = cursor.fetchmany
# result = cursor.fetchone
# result = cursor.fetchwarnings

# OUTPUT
# print(cursor.rowcount)
# print(cursor.column_names)
# print(cursor.arraysize)
# print(result)
#EXIT
input("\n\npress ENTER to exit")
os.system("cls")