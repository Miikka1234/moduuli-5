luku = int(input("Anna luku ja kerron onko se alkuluku:  "))
if luku % luku == 0 and luku % 1 == 0:
    print("Luku on alkuluku")
elif luku % 2 == 0 and luku % 3 == 0 and luku % 4 == 0 and luku % 5 == 0 and luku % 6 == 0 and luku % 7 == 0 and luku % 8 == 0 and luku % 9 == 0 and luku % 10 == 0:
    print("Luku ei ole alkuluku")