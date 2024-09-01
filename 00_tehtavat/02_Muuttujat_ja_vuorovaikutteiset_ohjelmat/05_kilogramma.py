#IDEA

# kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi
# ilmoittaa tuloksen käyttäjälle.

#     Yksi leiviskä on 20 naulaa.
#     Yksi naula on 32 luotia.
#     Yksi luoti on 13,3 grammaa.



import math

# INTRO
le:float = float(input("Anna leiviskät: "))
leg:float
n:float = float(input("Anna naulat: "))
ng:float
lu:float = float(input("Anna luodit: "))
lug:float

#LOGIC
if isinstance(le,float):
    leg = le*20*32*13.3
if isinstance(le,float):
    ng = n*32*13.3
if isinstance(le,float):
    lug = lu*13.3

g:float = leg+ng+lug
kg:int = math.floor(g/1000)
g = g-kg*1000

#OUTPUT
print("Massa nykymittojen mukaan:")
print("%.2f kilogrammaa ja %.2f grammaa." %(kg, g))

# print(leg)
# print(ng)
# print(lug)
# print("")
# print(g)
# print(kg)