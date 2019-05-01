# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 031 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
disvia = float(input('Digite a distancia em KM de sua viagem: '))
print()
if disvia <= 200:
    print('O preco da viagem por Km: R${}'.format(disvia * 0.50))
else:
    print('O preco da viagem por Km: R${}'.format(disvia * 0.45))

# ------ Footers ------ #
print(subfooter)
print(footer)
