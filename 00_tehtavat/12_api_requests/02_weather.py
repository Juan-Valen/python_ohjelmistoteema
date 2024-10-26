# -*- coding: utf-8 -*-
# IDEA
# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import os
from random import randint

import requests
# INTRO
os.system("cls")
# INPUT
city = input("Provide a city: ")
# LOGIC
api_key = "fe62546798b381967a15647210e08fb1"
request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fi"
# weather condition:
# description
# Kelvin to Celsius formula: C = K -273.15
# temperature (Celsius)
try:
    response = requests.get(request).json()
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")
    print(f"Error: {e}")
# OUTPUT
os.system("cls")
print(f"Country code: {response["sys"]["country"]}")
print(f"City: {response["name"]}")
print(f"Weather description: {response["weather"][0]["description"]}")
print(f"Temperature: {response["main"]["temp"]}{chr(176)} C")
print()
#EXIT
input("\n\npress ENTER to exit")
os.system("cls")

# coord
    # lon	24.9355
    # lat	60.1695
# weather
    # 0
        # id	803
        # main	"Clouds"
        # description	"broken clouds"
        # icon	"04d"
    # base	"stations"
# main
    # temp	284.83-273.15 = 11.68
    # feels_like	284.19
    # temp_min	284.13
    # temp_max	285.57
    # pressure	1020
    # humidity	82
    # sea_level	1020
    # grnd_level	1018
# visibility	10000
# wind
    # speed	6.26
    # deg	224
    # gust	7.6
# clouds	
    # all	75
# dt	1729853936
# sys
    # type	2
    # id	2011913
    # country	"FI"
    # sunrise	1729833936
    # sunset	1729867364
# timezone	10800
# id	658225
# name	"Helsinki"
# cod	200