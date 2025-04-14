import re

rv = re.compile(r"\d{9,10}")

data = ["9511121234", "9511121234 je rc"]

for d in data:
    m = rv.fullmatch(d)

    if m:
        print(f'"{d}" je v pořadku')
    else:
        print(f'"{d}" není v pořadku')
