# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio_024 ')
subfooter =('-'*68)
footer =('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
cty = (str(input('Digite o nome da Cidade: ')))
ctysp = cty.split()
print()
print('O nome da cidade digitada possiu "SANTO" em seu nome: {}'.format('SANTO' in ctysp[0]))

# ------ Footers ------ #
print(subfooter)
print(footer)
