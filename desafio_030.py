# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio_030 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
n1 = (int(input('Digite um numero: ')))
print()
result = (n1 % 2)
if result == 0:
    print('O numero {} e um numero PAR!'.format(n1))
else:
    print('O numero {} e um numero IMPAR!'.format(n1))

# ------ Footers ------ #
print(subfooter)
print(footer)
