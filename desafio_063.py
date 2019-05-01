# ------ Modules ------ #
from math import sqrt
from time import sleep

# ------ Header & Footers ------ #
header = str(' Desafio 063 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
rqoryn = 'Y'
while rqoryn not in 'Nn':
    rqfbmbr = (int(input('Digite o numero da sequencia de Fibonacci desejada: ')))
    print('Sera visualizada somente as 10 primeiras sequencias!')
    print()
    ctr = 1
    for x in range(1, 11):
        fbmbr = float(1.618034 ** rqfbmbr - (1 - 1.618034) ** rqfbmbr) / sqrt(5)
        print('\033[1;33m→\033[m {}'.format(round(fbmbr)), end=' ')
        rqfbmbr += 1
    print()
    print(subfooter)
    sleep(2)
    rqoryn = str(input("Digite 'Y' para continuar ou 'N' para sair do programa: "))
    print()

# ------ Footers ------ #
print(subfooter)
print(footer)
