# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 002 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
n1 = int(input('Digite um numero: '))
print()
print('O dobro de {} e: {}'.format(n1, n1 * 2))
print('O Triplo do numero digitado e: {}'.format(n1 * 3))
print('A raiz quadrada do numero digitado e: {:.2f}'.format(pow(n1, 1/2)))
print()

# ------ Footers ------ #
print(subfooter)
print(footer)