''' EUcsatlakozas.txt
Ausztria;1995.01.01
Belgium;1958.01.01
'''

class Eu:
  def __init__(self, sor):
    s = sor.strip().split(";")
    self.orszag = s[0]
    self.datum = s[1]
    self.ev = int(s[1][:4])
    self.honap = int(s[1][5:7])
    self.nap = int(s[1][8:10])

with open("EUcsatlakozas.txt", "r", encoding="latin2") as f:
  lista = [Eu(sor) for sor in f]