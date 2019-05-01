# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 002 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
medalt = float(input('Insert a altura: '))
medcom = float(input('Insert o comprimento: '))
medalcom = (medalt * medcom)
print()
print('Sera necessario {:.1f} litros de tinta para pintar {:.0f}m².'.format(medalcom / 2, medcom))

# ------ Footers ------ #
print(subfooter)
print(footer)
