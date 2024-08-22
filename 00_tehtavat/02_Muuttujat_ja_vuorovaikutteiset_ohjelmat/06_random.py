#IDEA
# kaksi numerolukon koodia:
#     3# koodin, 0..9 väliltä
#     4# koodin, 1..6 väliltä

import random
luko1 = []
luko2 = []

#LOGIC
while len(luko1)<3:
    luko1.append(random.randint(0,9))

while len(luko2)<4:
    luko2.append(random.randint(1,6))

#OUTPUT
print(f"lukko 1 on ", end="")
print(*luko1, sep = ", ")
print(f"lukko 2 on ", end="")
print(*luko2, sep = ", ")