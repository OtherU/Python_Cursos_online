# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 027 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
nme = str(input('Digite seu nome completo: ')).strip()
nmesp = nme.split()
print()
print('O primeiro nome digitado: {}'.format(nmesp[0]))
print('O sobrenome do nome digitado: {}'.format(nmesp[len(nmesp)-1]))

# ------ Footers ------ #
print(subfooter)
print(footer)

