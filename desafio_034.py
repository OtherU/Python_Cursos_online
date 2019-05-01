# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 034 ')
subfooter =('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
sal = float(input('Digite o valor de seu salario: '))
print()
if sal <= 1250:
    sal = (sal * 1.15)
else:
    sal = (sal * 1.10)
print(('Seu salario depois do aumento sera de: {:.2f}'.format(sal)))

# ------ Footers ------ #
print(subfooter)
print(footer)
