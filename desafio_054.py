# ------ Modules ------ #
from datetime import date

# ------ Header & Footers ------ #
header = str(' Desafio 054 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
cntu = 0
cntd = 0
for ppls in range(0, 4):
    name = str(input('Digite seu nome: '))
    birth = int(input('Digite sua data de nascimento: '))
    age = date.today().year - birth
    print()
    if age >= 21:
      cntu += 1
    else:
      cntd += 1
print('Entre 8 pessoas cadastradas:\nMAIORES= {}\nMENORES= {}'.format(cntu, cntd))

# ------ Footers ------ #
print(subfooter)
print(footer)
