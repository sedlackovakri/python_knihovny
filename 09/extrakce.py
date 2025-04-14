import re

zapis = """
Zápisy o provedených vyšetřeních:
Pacient 6407156800 trpěl bolestí zad a byl poslán na vyšetření. 
Pacientka 8655057477 přišla na kontrolu po zranění kotníku.
Do ordinace telefonovala pacientka 7752126712, které byl elektronicky vydán recept na Paralen. 
"""

rv = re.compile(r"\d{9,10}")

# vystup = rv.findall(zapis)
# print(vystup)
# 
# print(rv.sub("X" * 9, zapis))

m = rv.search(zapis)
print(m.group())