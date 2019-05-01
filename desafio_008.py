# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 002 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
valor = float(input('Digite um valor em metro que deseja converter em outras unidades de comprimento: '))
print('Valor convertido para kilometros: {}'.format(valor / 1000))
print('Valor convertido para hectometro: {}'.format(valor / 100))
print('Valor convertido para decametro: {}'.format(valor / 10))
print('Valor convertido para decimetro: {}'.format(valor * 10))
print('Valor convertido para centimetros: {}'.format(valor * 100))
print('Valor convertido para milimetros: {}'.format(valor * 1000))
print()

# ------ Footers ------ #
print(subfooter)
print(footer)
