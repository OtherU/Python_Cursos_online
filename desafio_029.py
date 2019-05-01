# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio_029 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
velo = float(input('Digite a velocidade do carro: '))
print()
if velo >= 80:
    print('Voce foi multado por ultrapassar a velocidade de 80Km/h')
    print('Valor da multa: R${:.2f}'.format(float((velo - 80) * 7.00)))

# ------ Footers ------ #
print(subfooter)
print(footer)
