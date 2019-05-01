# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 049 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
n = int(input('Digite o numero da tabuada desejada: '))
print()
print('Criar a tabuada do {}'.format(n))
for tb in range(0, 11):
    print('|{} x {} = {}'.format(n, tb, (n * tb)))

# ------ Footers ------ #
print(subfooter)
print(footer)
