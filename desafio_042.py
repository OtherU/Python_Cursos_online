# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 042 ')
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
    print('As retas PODEM formar um triangulo, ', end='')
    if ret1 == ret2 == ret3:
        print('\033[1;33mEquilatero\033[m!')
    elif ret1 != ret2 != ret3:
        print('\033[1;35mEscaleno\033[m!')
    else:
        print('\033[1;32mIsosceles\033[m!')
else:
    print('As retas \033[1;31mNAO PODEM\033[m formar um triangulo!')

# ------ Footers ------ #
print(subfooter)
print(footer)
