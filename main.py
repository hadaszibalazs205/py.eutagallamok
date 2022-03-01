''' EUcsatlakozas.txt
Ausztria;1995.01.01
Belgium;1958.01.01
'''
#1. és 2. feladat

class Eu:
  def __init__(self, sor):
    orszag, datum = sor.strip().split(";")
    self.orszag = orszag
    self.datum = datum
    self.ev = int(datum[:4])
    self.honap = int(datum[5:7])
    self.nap = int(datum[8:10])
lista = []
with open("EUcsatlakozas.txt", "r", encoding="latin2") as f:
  for sor in f:
    lista.append(Eu(sor))

#3.feladat: Tagállamok száma

print(f"3. feladat: Eu tagállamok száma: {len(lista)} db")

#4.feladat: 2007-ben csatlakozott orzságok száma

szamlalo = 0

for sor in lista:
  if sor.ev == 2007:
    szamlalo += 1
print(f"4. feladat: 2007-ben {szamlalo} ország csatalakozott")

#5.feladat: Magyarország csatlakozásának dátuma

csatlakozasi_datum = ""
for sor in lista:
  if sor.orszag == "Magyarország":
    csatlakozasi_datum = sor.datum
print(f"5. feladat: Magyarország csatalkozási dátuma: {csatlakozasi_datum}")

#6.feladat: Májusban történt-e csatlakozás

szamlalo2 = 0

for sor in lista:
  if sor.honap == 5:
    szamlalo2 += 1
if szamlalo2 > 0:
  print(f"6. feladat: Májusban volt csatlakozás")
else:
  print(f"6. feladat: Májusban nem volt csatlakozás")

#7.feladat: Legutoljára csatlakozott ország

utolso = ""
for sor in lista:
  if sor.datum > utolso:
    utolso = sor.datum
    utolso_sor = sor
print(f"7. feladat: A legutoljára csatlakozott ország {utolso_sor.orszag}")

#8.feladat: Statisztika

stat = dict()
for sor in lista:
  stat[sor.ev] = stat.get(sor.ev, 0) + 1

print(f"8 feladat: Statisztika")
for kulcs, ertek in stat.items():
  print(f"       {kulcs} - {ertek} ország")