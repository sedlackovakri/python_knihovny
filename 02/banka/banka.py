# Nasimulujte bankovní systém
#
# V adresáři jsou soubory pojmenované číslem účtu obsahující zůstatek účtu
# Implementujte skript banka.py, který bude ovládán parametry:
#
# Částka se bude čerpat z účtu 111 pomocí --from 111
# Částka se bude připisovat na účet 222 pomocí --to 222
# Převod částky 1000 se určí parametrem --amount 1000
#
# Snažte se řešit různé chyby:
# * účet neexistuje
# * zůstatek by šel do záporu
#
# Příklad použití:
#
#   python banka.py --from 111 --to 222 --amount 1000
#
# V praxi se píší skripty, kde nezáleží na pořadí pojmenovaných parametrů, tj.
# ideální je, když funguje libovolné pořadí parametrů při spuštění:
#
#   python banka.py --from 111 --amount 1000 --to 222
#   python banka.py --amount 1000 --from 111 --to 222
#
# Pro tento pokročilý způsob je však třeba použít pokročilou knihovnu pro práci
# s parametry příkazové řádky, jako např. argparse nebo click.


import argparse 

def get_balance(account_number):
    try:
        file = open(str(account_number))
        balance = file.read()
        file.close() 
        return int(balance)
    except FileNotFoundError:
        return f"Chyba: Účet s číslem {account_number} neexistuje."

def update_balance(account_number, amount): 
    file = open(str(account_number), "w")
    file.write(str(amount))

def transfer_amount(from_account_number, to_account_number, amount):
    amount = int(amount)
    new_balance_from = get_balance(from_account_number)
    new_balance_to = get_balance(to_account_number)

    if amount <= 0:
        raise ValueError("Lze zadat pouze zadat kladnou částku.")

    if new_balance_from < amount: 
        raise ValueError("Na účtě není dostatek peněz.")
    
    if from_account_number == to_account_number:
        raise ValueError("Účet příjemce a odesílatele nesmí být stejný.")
        
    new_balance_from -= amount 
    update_balance(from_account_number, new_balance_from)
    new_balance_to += amount
    update_balance(to_account_number, new_balance_to)  


parser = argparse.ArgumentParser() 
parser.add_argument("--from", type=int, required=True, dest="from_account")
parser.add_argument("--to", type=int, required=True, dest="to_account")
parser.add_argument("--amount", type=int, required=True, dest="amount")
 
arguments = parser.parse_args() 

from_account_number = arguments.from_account
to_account_number = arguments.to_account
amount = arguments.amount  

transfer_amount(from_account_number, to_account_number, amount)
print(f"Úspěšně převedeno {amount} z účtu {from_account_number} na účet {to_account_number}.")