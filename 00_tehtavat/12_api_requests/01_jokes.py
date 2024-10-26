# IDEA
# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. 
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/. 
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

import os
import requests
# INTRO
os.system("cls")
# INPUT
# LOGIC
try:
    request: str = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request).json()
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")
    print(f"Error: {e}")
# OUTPUT
print(response["value"])
print()
#EXIT
input("\n\npress ENTER to exit")
os.system("cls")