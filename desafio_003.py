# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 003 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
n1 = int(input('Insert the first number: '))
n2 = int(input('Insert the second number: '))
soma = n1 + n2
print()
print('A soma de {0} e {1} e igual a {2}'.format(n1, n2, soma))

# ------ Footers ------ #
print(subfooter)
print(footer)
