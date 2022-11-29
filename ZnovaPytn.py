# znovu si zkouším programovat cvičení z itnetwork.cz a  Checkio.org
cisla = []
cislo = "cokoliv"

#začnu od konce, tj. prázdno
while cislo:
      cislo = input("Zadej číslo: ")
      if cislo != " ":
            cisla.append(int(cislo))
cisla_2 = sorted(cisla)
# zjednodušený medián
median = cisla_2[len(cisla_2)//2]
for cislo in cisla:
    print(cislo, "se od mediánu odlišuje o", cislo - median)
