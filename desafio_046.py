# ------ Modules ------ #
from time import sleep

# ------ Header & Footers ------ #
header = str(' Desafio 046 ')
subfooter = ('-' * 68)
footer = ('=' * 68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
print('''Configurar a contagem regressiva para os fogos de artificios.
[ 1 ] Contagem de 3sec.
[ 2 ] Contagem de 5sec.
[ 3 ] Contagem de 10sec. ''')
cnt = int(input('Digite uma opcao: '))
print()
print('Countdown Starting...')
if cnt == 1:
    for rpt in range(3, 0, -1):
        print(rpt)
        sleep(1)
elif cnt == 2:
    for rpt in range(4 + 1, 0, -1):
        print(rpt)
        sleep(1)
elif cnt == 3:
    for rpt in range(10, 0, -1):
        print(rpt)
        sleep(1)
else:
    print()
    print('Option \033[1;31mINVALID!\033[m')
if 0 < cnt < 4:
    print()
    print('\033[1;33mBOOM\033[m, ', end='')
    print('\033[1;34mHAPPY NEW YEAR!!!\033[m')

# ------ Footers ------ #
print(subfooter)
print(footer)
