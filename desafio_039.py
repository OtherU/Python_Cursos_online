# ------ Modules ------ #
from datetime import date

# ------ Header & Footers ------ #
header = str(' Desafio 039 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
birdat = int(input('Digite o ano da data de seu nascimento: '))
today = date.today().year
if today - birdat < 18:
    print()
    print('Voce ainda vai se alistar ao servico militar!')
elif today - birdat == 18:
    print()
    print('\033[34mVoce ira se alistar este \033[4;34mano\033[34m ao servico militar!\033[m')
else:
    print()
    print('\033[1;31mJa passou o ano de se alistar ao service militar!\033[m')

# ------ Footers ------ #
print(subfooter)
print(footer)
