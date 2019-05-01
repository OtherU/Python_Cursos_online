# ------ Modules ------ #

# ------ Header & Footers ------ #
header = (' Desafio 012 ')
footer = ('='*68)
subfooter = ('-'*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
valprod = (float(input('Digite o valor atual do produto:R$ ')))
print('O valor do produto com 5% de desconto:R$ {:.2f}'.format(valprod - (valprod * 0.05)))

# ------ Footers ------ #
print(subfooter)
print(footer)
