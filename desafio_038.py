# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 038 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print()
    print('O primeiro valor ({}) e maior!'.format(n1))
elif n2 > n1:
    print()
    print('O segundo valor ({}) e maior'.format(n2))
else:
    print()
    print('Nao existe valor maior, os dois sao iguais!')

# ------ Footers ------ #
print(subfooter)
print(footer)
