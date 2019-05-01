# ------ Modules ------ #


# ------ Header & Footers ------ #
header = (' Desafio 013 ')
footer = ('='*68)
subfooter = ('-'*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
salatu = (float(input('Digite o valor de seu salario atual: R$ ')))
print('Seu salario com 15% de aumento sera de: R$ {:.2f}'.format(float(salatu * 1.15)))

# ------ Footers ------ #
print(subfooter)
print(footer)
