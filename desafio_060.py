# ------ Modules ------ #
from time import sleep

# ------ Header & Footers ------ #
header = str(' Desafio 060 ')
subfooter = str('-' * 68)
footer = str('=' * 68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
ctnmb = 1
ftnmb = 1
rqnmb = int(input('Digite um numero: '))
print('Processing...')
for tme in range(1, 4):
    print('-', end='')
    sleep(0.5)
print('>')
print()
for rgnmb in range(rqnmb, 0, - 1):
    ctnmb = rgnmb - 1
    ftnmb += ftnmb * ctnmb
print('O fatorial de {}!: {}'.format(rqnmb, ftnmb))

# ------ Footers ------ #
print(subfooter)
print(footer)
