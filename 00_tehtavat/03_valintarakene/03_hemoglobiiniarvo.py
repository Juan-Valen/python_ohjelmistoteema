
    # Kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). 
    # Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
    #     Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
    #     Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

import os


os.system("cls")
#INPUT
sukupuoli = input("Anna sukupuolesi (nainen tai mies): ")
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvosi (g/l): "))

#LOGIC
if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("\nHemoglobiiniarvosi on alhainen")
    elif hemoglobiiniarvo > 175:
        print("\nHemoglobiiniarvosi on korkea")
    else:
        print("\nHemoglobiiniarvosi on normaali")
elif sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("\nHemoglobiiniarvosi on alhainen")
    elif hemoglobiiniarvo > 195:
        print("\nHemoglobiiniarvosi on korkea")
    else:
        print("\nHemoglobiiniarvosi on normaali")

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")