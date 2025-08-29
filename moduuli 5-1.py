#ohjelma joka kysyy arpakuutioiden määrän, heittää arpakuutiot ja antaa niiden lukujen summan
import random


nopat = int(input("Kuinka monta noppaa heitetään:"))
summa = 0
for nopat in range(nopat):
    silmäluku = random.randint(1,6)
    summa += silmäluku

print(f"Summa     = {summa}")
if nopat >1:
    print(f"Keskiarvo = {summa / nopat}")

