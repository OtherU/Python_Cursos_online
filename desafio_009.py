# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 002 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
numbtab = int(input('Digite qual tabela de tabuada deseje: '))
print('{} x {:2} = {}'.format(numbtab, 1, (numbtab * 1)))
print('{} x {:2} = {}'.format(numbtab, 2, (numbtab * 2)))
print('{} x {:2} = {}'.format(numbtab, 3, (numbtab * 3)))
print('{} x {:2} = {}'.format(numbtab, 4, (numbtab * 4)))
print('{} x {:2} = {}'.format(numbtab, 5, (numbtab * 5)))
print('{} x {:2} = {}'.format(numbtab, 6, (numbtab * 6)))
print('{} x {:2} = {}'.format(numbtab, 7, (numbtab * 7)))
print('{} x {:2} = {}'.format(numbtab, 8, (numbtab * 8)))
print('{} x {:2} = {}'.format(numbtab, 9, (numbtab * 9)))
print('{} x {:2} = {}'.format(numbtab, 10, (numbtab * 10)))

# ------ Footers ------ #
print(subfooter)
print(footer)