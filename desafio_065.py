# ------ Modules ------ #
from time import sleep

# ------ Header & Footers ------ #
header = str(' \033[1;32mDesafio 065\033[m ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
somnmb = 0
rq_yn = 'Y'
mjnmb = 0
mnmb = 0
ctr = 0
while rq_yn not in 'Nn':
    rqnmbr = int(input('Digite um numero: '))
    print()
    somnmb += rqnmbr
    ctr += 1
    if rqnmbr > mjnmb:
        mjnmb = rqnmbr
    if rqnmbr < mnmb or mnmb == 0:
        mnmb = rqnmbr
    rq_yn = str(input("\033[1;33mDigite 'N' para visualizar o resultado ou 'Y' para continuar!\033[m\nDigite 'Y/N': "))
    print()
print(subfooter)
print('Processing...')
for tic_tac in range(1, 4):
    sleep(0.5)
    print('-', end='')
print('>')
print(str('\033[1;34m【Vizualizar Resultado dos numeros digitados!】\033[m'))
print('(1) Media dos Numeros: {:.0f}\n(2) O Maior Numero: {}\n(3) O Menor Numero: {}'.format(somnmb / ctr, mjnmb, mnmb))

# ------ Footers ------ #
print(subfooter)
print(footer)
