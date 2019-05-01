# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 048 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
print('Display numbers between 1 to 500, only the odds divisible for 3 ')
print()
smos = 0
cntr = 0
for cntos in range(1, 501, 2):
    if cntos % 3 == 0:
        print(cntos, end=' ')
        smos += cntos
        cntr += 1
print()
print('...Ending Count, the sum between the {} numbers counted is: {}'.format(cntr, smos))

# ------ Footers ------ #
print(subfooter)
print(footer)
