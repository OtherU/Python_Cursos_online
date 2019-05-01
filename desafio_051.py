# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 051 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
trm1 = int(input('Digite o primeiro termo: '))
rs = int(input('Digite a razao: '))
ne = trm1 + (10 - 1) * rs
print()
for t1lp in range(trm1, ne+1, rs):
    print('\033[1;33m→ \033[m{}'.format(t1lp), end=' ')
print()

# ------ Footers ------ #
print(subfooter)
print(footer)
