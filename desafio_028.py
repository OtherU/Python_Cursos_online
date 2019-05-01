# ------ Modules ------ #
from random import randrange

# ------ Header & Footers ------ #
header = str(' Desafio 028 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
n1c = int(randrange(5))
pler = str(input('Digite o nome do jogador: '))
n2p = int(input('Adivinhe o numero escolhido pelo PC de 0 a 5: '))
print()
if n1c == n2p:
    print('{}, YOU WIN!!!'.format(pler))
else:
    print('YOU LOSE!!!')
    print('O numero escolhido pelo PC: "{}"'.format(n1c))

# ------ Footers ------ #
print(subfooter)
print(footer)
