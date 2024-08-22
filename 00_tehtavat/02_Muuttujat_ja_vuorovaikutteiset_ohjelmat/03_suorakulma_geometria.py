# IDEA

# kysyy suorakulmion kannan ja korkeuden.
# tulostaa suorakulmion piirin ja pinta-alan.
#   Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

#INPUT
print("Suorakulma:")
width = float(input("  Leveys: "))
height = float(input("  Korkeus: "))
#LOGIC
surface = (height*2) + (width*2)
area = height*width
#OUTPUT
print("\nSuorakulma: ")
print(f"  piiri on {surface:.2f}m")
print(f"  pinta-ala on {area:.2f}m2")


