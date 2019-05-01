# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 050 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
smct = 0
for cnt in range(0, 6):
    n1 = (int(input('Digite um numero: ')))
    if n1 % 2 == 0:
        smct += n1
    else:
        print('O numero digitado {} e impar, portanto \033[1;31mNAO\033[m sera somado!'.format(n1))
print()
print('A soma dos numeros pares digitados: \033[1;33m{}\033[m'.format(smct))

# ------ Footers ------ #
print(subfooter)
print(footer)
