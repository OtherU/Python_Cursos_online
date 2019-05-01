# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 002 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
money = float(input('Digite o valor em reais(R$) que gostaria de converter para dollares(US$): '))
print()
print('Quantia convertida para dollares sera de: ${:.2f}'.format(money / 3.27))

# ------ Footers ------ #
print(subfooter)
print(footer)
