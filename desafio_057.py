# ------ Modules ------ #
from time import sleep

# ------ Header & Footers ------ #
header = str(' Desafio 057 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
nme = str(input('Digite um nome: ')).strip().title()
sex = str(input('Digite o sexo(M/F): ')).upper()[0]
while sex not in 'MmFf':
    print('option invalid. choose["M" or "F"] and try again!')
    sleep(2)
    print()
    if sex != 'MmFf':
        nme = str(input('Digite um nome: ')).strip().title()
        sex = str(input('Digite o sexo(M/F): ')).strip().upper()[0]
print()
print(subfooter)
print('NAME= \033[1;34m{}\033[m\nSEXO= \033[1;34m{}\033[m'.format(nme, sex))

# ------ Footers ------ #
print(subfooter)
print(footer)