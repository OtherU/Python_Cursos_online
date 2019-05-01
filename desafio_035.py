# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 035 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
ret1 = float(input('Digite o comprimento da primeira reta: '))
ret2 = float(input('Digite o comprimento da segunda reta: '))
ret3 = float(input('Digite o comprimento da terceira reta: '))
print()
if ret1 < ret2 + ret3 and ret2 < ret1 + ret3 and ret3 < ret1 + ret2:
    print('As retas PODEM formar um triangulo!')
else:
    print('As retas NAO PODEM formar um triangulo!')

# ------ Footers ------ #
print(subfooter)
print(footer)
