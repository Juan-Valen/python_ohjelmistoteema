print("Antaa kolme numero:")
summa: float = 0
tulo: float = 1
keskiarvo: float = 0
i = 0
while i<3:
  ++i
  n = float(input("  Anna numero: "))
  if isinstance(n,float):
    summa+=n
    tulo*=n
keskiarvo= summa/3

print("")
print("Lukujen:")
print("  Summa: %.2f" % (summa))
print("  Tulo: %.2f" % (tulo))
print("  Keskiarvo: %.2f" % (keskiarvo))
