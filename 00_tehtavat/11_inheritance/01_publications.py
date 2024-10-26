# IDEA
# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. 
# Jokaisella julkaisulla on nimi. 
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. 
# Kirjoita luokkiin myös tarvittavat alustajat. 
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. 
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). 
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

import os
from random import randint
# INTRO
os.system("cls")

class Publication:
    def __init__(self, name: str) -> None:
        self.name = name
    def print_information(self):
        print(f"Name: {self.name}")
class Book(Publication):
    def __init__(self, name: str, author: str, page_count: int) -> None:
        self.author = author
        self.page_count = page_count
        super().__init__(name)
    def print_information(self):
        super().print_information()
        print(f"Pages: {self.page_count}\nAuthor: {self.author}")
class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str) -> None:
        self.chief_editor = chief_editor
        super().__init__(name)
    def print_information(self):
        super().print_information()
        print(f"Chief director: {self.chief_editor}")


# INPUT
# LOGIC
m = Magazine("Donalnd Duck", "Aki Hyyppä")
b = Book("Compartment No. 6", "Rosa Liksom", 192)

m.print_information()
b.print_information()
# OUTPUT
#EXIT
input("\n\npress ENTER to exit")
os.system("cls")