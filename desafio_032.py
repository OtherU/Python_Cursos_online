# ------ Modules ------ #
from datetime import date

# ------ Header & Footers ------ #
header = str(' Desafio 032 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
ano = int(input('Digite 0 para analisar o ano atual ou digite um ano: '))
print()
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} e um ano bixesto!'.format(ano))
else:
    print('O ano {} NAO e um ano bixesto!'.format(ano))

# ------ Footers ------ #
print(subfooter)
print(footer)
