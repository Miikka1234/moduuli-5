#kysytään 5 kaupungin nimet ja listataan ne allekkain, for ja in komennoilla
print("Anna 5 kaupungin nimeä!")
kaupungit = []
a = input("1")
kaupungit.append(a)
b = input("2")
kaupungit.append(b)
c = input("3")
kaupungit.append(c)
d = input("4")
kaupungit.append(d)
e = input("5")
kaupungit.append(e)
for nimet in kaupungit:
    print(nimet)