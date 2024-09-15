# IDEA
# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. 
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. 
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import os
from random import randint
import mysql.connector


def find_airport():
    icao_koodi: str = None
    while not icao_koodi:
        # INPUT
        os.system("cls")
        icao_koodi = input("Anna lentoasema ICAO-koodi: ")
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
    cursor.execute(f"SELECT name FROM airport WHERE ident = '{icao_koodi}';")
    result = cursor.fetchall()
    for row in result:
        print(row)
# INTRO
os.system("cls")
# LOGIC
find_airport()

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")