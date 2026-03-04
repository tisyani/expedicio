f = open("veetel.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

class vetel:
    def __init__(self, nap, amator, uzenet):
        self.nap = int(nap)
        self.amator = int(amator)
        self.uzenet = uzenet

print("ELSO FELADAT")

vetelek = []

for i in range(0, len(sorok), 2):
    darabok = sorok[i].strip().split()
    v = vetel(darabok[0], darabok[1], sorok[i+1])
    vetelek.append(v)

print(f"Elso uzenet rogzitoje: {vetelek[0].amator}")
print(f"utolso uzenet rogzitoje: {vetelek[-1].amator}")

print("MASODIK FELADAT")

for v in vetelek:
    if v.uzenet.__contains__("farkas"):
        print(f"farkas uzenet rogzitoje: {v.amator}, napja: {v.nap}")

print("HARMADIK FELADAT")

for nap in range(1, 12):
    db = 0
    for v in vetelek:
        if v.nap == nap:
            db += 1
    print(f"{nap}. nap: {db} uzenet")

print("NEGYEDIK FELADAT")
f = open("adaas.txt", "w", encoding="utf-8")

for nap in range(1, 12):
    alap = ["#"] * 90
    for v in vetelek:
        if v.nap == nap:
            u = v.uzenet.rstrip("\n")
            for i in range(min(len(u), 90)):
                if u[i] != "#":
                    alap[i] = u[i]
    print(f"{nap}. nap: {''.join(alap)}")


f.close()

nap = int(input("irj be egy napot: "))
amator = int(input(" irj be egy amatort: "))

vizsgalando = ""
for v in vetelek:
    if v.nap == nap and v.amator == amator:
        vizsgalando = v.uzenet.split(" ")[0]

if vizsgalando == "":
    print("nincs ilyen uzenet")
else:
    darabok = vizsgalando.split("/")
    if len(darabok) != 2:
        print("nincs informacio")
    else:
        if (darabok[0].isdigit() and darabok [1].isdigit()):
            print(int(darabok[0]) + int(darabok[1]))
        else:
            print("nincs informacio")