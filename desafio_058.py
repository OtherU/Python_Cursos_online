# ------ Modules ------ #
from random import randrange
from time import sleep

# ------ Header & Footers ------ #
header = str(' Desafio 058 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
pin = '-'
n1c = int(randrange(2))
pler = str(input('Digite o nome do jogador: ')).strip().title()
n2p = int(input('Adivinhe o numero escolhido pelo PC de 0 a 10: '))
cnt = 0
print('Processing...')
for i in range(1, 4):
    print('{}'.format(pin), end='')
    sleep(1)
print('>')
print()
if n1c == n2p:
    print('{}, \033[1;33mYOU WIN!!!\033[m\nTries: {}'.format(pler, cnt))
    cnt += 1
else:
    while n1c != n2p:
        pler = str(input('\033[1;5;31mTente novamente!!!\033[m\nDigite o nome do jogador: ')).strip().title()
        n2p = int(input('Adivinhe o numero escolhido pelo PC de 0 a 10: '))
        print('Processing...')
        cnt += 1
        for i in range(1, 4):
            print('{}'.format(pin), end='')
            sleep(1)
        print('>')
        print()
    print('{}, \033[1;33mYOU WIN!!!\033[m\nTries: {}'.format(pler, cnt))

# ------ Footers ------ #
print(subfooter)
print(footer)