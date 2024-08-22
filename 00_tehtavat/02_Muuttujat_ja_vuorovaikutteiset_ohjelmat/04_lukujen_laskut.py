# IDEA

# Kysyy kolme kokonaislukua
# Tulostaa lukujen summan, tulon ja keskiarvon.

# INTRO
print("Antaa kolme numero:")
summa: float = 0
tulo: float = 1
keskiarvo: float = 0
# LOGIC
i = 0
while i<3:
  ++i
  # INPUT
  n = int(input("  Anna numero: "))
  # LOGIC
  if isinstance(n,float):
    summa+=n
    tulo*=n
keskiarvo= summa/3
# OUTPUT
print("")
print("Lukujen:")
print(f"  Summa: {summa:.2f}")
print(f"  Tulo: {tulo:.2f}")
print(f"  Keskiarvo: {keskiarvo:.2f}")
