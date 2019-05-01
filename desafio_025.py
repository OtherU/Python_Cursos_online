# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 025 ')
subfooter = str('-'*68)
footer = str('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
nme = str(input('Digite o nome completo: '))
nmesp = nme.split()
print()
print('No nome digitado existe o nome "SILVA": {}'.format('SILVA' in nmesp[::]))

# ------ Footers ------ #
print(subfooter)
print(footer)

