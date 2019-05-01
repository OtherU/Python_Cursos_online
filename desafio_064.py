# ------ Modules ------ #
from time import sleep

# ------ Header & Footers ------ #
header = str(' Desafio 064 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
ctr = 0
snmbr = 0
rqnmbr = 0
print("Digite um numero inteiro para somar seus valores ou '999' para sair!")
while rqnmbr != 999:
    rqnmbr = int(input('Digite um numero: '))
    if rqnmbr != 999:
        snmbr += rqnmbr
        ctr += 1
    print()
    print(subfooter)
print('Processing...')
sleep(1.5)
for tic_tac in range(1, 4):
    print('-', end='')
print('>')
print()
print('A Soma: {}\nQuant. de Numeros Digitados: {}'.format(snmbr, ctr))

# ------ Footers ------ #
print(subfooter)
print(footer)
