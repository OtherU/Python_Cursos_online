# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 043 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
alt = float(input('Digite sua altura: '))
pes = float(input('Digite seu peso: '))
imc = pes / (alt ** 2)
print()
if imc < 18.5:
    print('Voce esta \033[1;36mABAIXO\033[m do peso!')
elif 18.4 < imc < 25.1:
    print('Voce esta com o \033[1;34mPESO IDEAL\033[m')
elif 24 < imc < 31:
    print('Voce esta \033[1;33mSOBREPESO!\033[m')
elif 29 < imc < 41:
    print('Voce esta com \033[1;35mOBESIDADE!\033[m')
else:
    print('Voce esta com \033[1;31mOBESIDADE MORBIDA!\033[m')

# ------ Footers ------ #
print(subfooter)
print(footer)
