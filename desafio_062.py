# ------ Modules ------ #
from time import sleep

# ------ Header & Footers ------ #
header = str(' Desafio 061 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
ct = 1
rqt = "1"
while rqt is not 0:
    print('Processing...')
    for tic in range(1, 4):
        print('-', end='')
        sleep(0.5)
    print('>')
    print()
    trm1 = int(input('Digite o primeiro termo: '))
    rs = int(input('Digite a razao: '))
    print()
    while ct <= 10:
        ct += 1
        print('\033[1;33m→ \033[m{}'.format(trm1), end=' ')
        trm1 += rs
    break
    print()
rqt = input('Digite "0"(zero) para sair do programa!: ')
for tac in range(1, 4):
    print('.', end='')
    sleep(0.5)
print('Saindo do programa!')
# ------ Footers ------ #
print(subfooter)
print(footer)
#Melhore o Desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termo.