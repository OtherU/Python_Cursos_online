# ------ Modules ------ #
from math import ceil

# ------ Header & Footers ------ #
header = (' Desafio 016 ')
footer = ('='*68)
subfooter = ('-'*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
num1 = float(input('Digite qualquer numero: '))
print('O numero digitado em sua porcao inteira e: {}'.format(ceil(num1)))

# ------ Footers ------ #
print(subfooter)
print(footer)
