# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 023 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
numb = (int(input('Digite um numero: ')))
print('A unidade do numero {}: {}'.format(numb, numb // 1 % 10))
print('A dezena  do numero {}: {}'.format(numb, numb // 10 % 10))
print('A centena do numero {}: {}'.format(numb, numb // 100 % 10))
print('A milhar  do numero {}: {}'.format(numb, numb // 1000 % 10))

# ------ Footers ------ #
print(subfooter)
print(footer)
