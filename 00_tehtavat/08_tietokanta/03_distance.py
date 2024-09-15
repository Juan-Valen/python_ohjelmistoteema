# IDEA
# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. 
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. 
    # Laskenta perustuu tietokannasta haettuihin koordinaatteihin. 
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/. 
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. 
# Kirjoita hakukenttään geopy ja vie asennus loppuun.



from ast import Return
import os
from random import randint
import mysql.connector
from geopy import distance



def get_coordinates():
    icao_koodi: str = None
    while not icao_koodi:
        # INPUT
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
    cursor.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_koodi}';")
    result = cursor.fetchall()
    return result[0]
# INTRO
os.system("cls")
print("This program will measure the distance between 2 airports.\n\n")
# LOGIC

print("First airport:")
coordinate_1 = get_coordinates()
print("Second airport:")
coordinate_2 = get_coordinates()

print(F"The distance between the two airports is {distance.distance(coordinate_1, coordinate_2).meters/1000} km")

# OUTPUT

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")