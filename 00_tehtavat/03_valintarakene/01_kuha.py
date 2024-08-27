
# IDEA

    # kysyy kalastajalta kuhan pituuden senttimetreinä
    #  Jos kuha on alamittainen
    # Kuha on alamittainen, jos sen pituus on alle 37 cm.
        # käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
import os


os.system("cls")
#INPUT
kuhan_pituus = float(input("Anna kuhan pituuden (cm): "))

#LOGIC
if kuhan_pituus < 37:
    print("\n\nKäskee laskea kuhan takaisin järveen.")
    print(f"\nkuhan pituus puuttuu {37-kuhan_pituus}cm")

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")