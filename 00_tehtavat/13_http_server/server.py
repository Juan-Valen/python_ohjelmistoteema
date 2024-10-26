import json
from flask import Flask, jsonify
import mysql.connector

# ---------------------
#   CONFIGURATION
# ---------------------
app = Flask(__name__)
# ---------------------
#   FUNCTIONS
# ---------------------
def find_airport(icao: str):
    # CREATE OR REPLACE USER dbuser IDENTIFIED BY 'sAL_a3ana';
    # GRANT SELECT ON flight_game.airport to 'dbuser';
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
    cursor.execute(f"SELECT ident AS 'ICAO', Name, municipality AS 'Location' FROM airport WHERE ident = '{icao}';")
    airports = list(cursor.fetchone())
    return airports

# ---------------------
#   ROUTES
# ---------------------
# IDEA
# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. 
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. 
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. 
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

@app.route("/prime_number/<number>")
def PrimeNumbers(number: int):
    number = int(number)
    isPrime = False
    # LOGIC
    if int(number) in [2, 3, 5, 7]:
        isPrime = True
    if (not(int(number) % 2 == 0 or int(number) % 3 == 0 or int(number) % 5 == 0 or int(number) % 7 == 0)):
        isPrime = True
    return {"Number": number, "isPrime": isPrime}

# IDEA
# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa. 
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. 
    # Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. 
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

@app.route("/airport/<icao>")
def airport(icao: str):
    airports = find_airport(icao)
    print("AIRPORTS LIST JSON:")
    return {'ICAO': airports[0], 'Name': airports[1], 'Location': airports[2]}
# ---------------------
#   CONFIGURATION
# ---------------------
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
