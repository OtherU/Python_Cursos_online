# ------ Modules ------ #
from time import sleep

# ------ Header & Footers ------ #
header = str(' Desafio 061 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
trm1 = int(input('Digite o primeiro termo: '))
rs = int(input('Digite a razao: '))
ct = 1
print()
print('Processing...')
for tim in range(1, 4):
    print('-', end='')
    sleep(0.5)
print('>')
while ct <= 10:
    ct += 1
    print('\033[1;33m→ \033[m{}'.format(trm1), end=' ')
    trm1 += rs
print()

# ------ Footers ------ #
print(subfooter)
print(footer)
