# ------ Modules ------ #

# ------ Header & Footers ------ #
header = (' Desafio 022 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
nomeco = input('Digite seu nome completo: ').strip()
print()
print("In upper-case version")
print(nomeco.upper())
print(subfooter)
print("In lower-case version")
print(nomeco.lower())
print(subfooter)
print('O seu nome inteiro tem um total de {} letras'.format(len(nomeco)))
print(subfooter)
div = nomeco.split()
print('O primeiro nome {} tem: {} letras'.format(div[0], len(div[0])))

# ------ Footers ------ #
print(subfooter)
print(footer)



