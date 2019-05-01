# ------ Modules ------ #
from time import sleep

# ------ Header & Footers ------ #
header = str(' Desafio 052 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
inm = (int(input('Digite um numero: ')))
print('Avaliando o numero digitado...')
ctr = 0
sleep(1)
print()

for ctg in range(1, inm + 1):
    if inm % ctg == 0:
        print('\033[1;33m', end=' ')
        ctr += 1
    else:
        print('\033[1;30m', end=' ')
    print('{}'.format(ctg), end=' ')
print('\033[m')

if ctr == 2:
    print('O numero {} e um \033[1;34mnumero PRIMO!\033[m'.format(inm))
else:
    print('O numero {} \033[1;31mNAO\033[m e um numero PRIMO!'.format(inm))
ctr += 1

# ------ Footers ------ #
print(subfooter)
print(footer)
