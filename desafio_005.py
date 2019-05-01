# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 002 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
n1 = int(input('Digite um numero: '))
print('O Sucessor do primeiro numero digitado: {}'.format(n1 + 1))
print('O Antecessor do numero digitado: {}'.format(n1 - 1))

# ------ Footers ------ #
print(subfooter)
print(footer)


