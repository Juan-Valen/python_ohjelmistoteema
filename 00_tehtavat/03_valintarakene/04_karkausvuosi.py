
# kysyy vuosiluvun ja 
# ilmoittaa, onko annettu vuosi karkausvuosi
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

import os


os.system("cls")
#INPUT
vuosi = int(input("Anna vuosi: "))

#LOGIC
if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        print("vuosi on karkausvuosi.")
elif vuosi % 4 == 0:
    print("vuosi on karkausvuosi.")

#EXIT
input("\n\npress ENTER to exit")
os.system("cls")