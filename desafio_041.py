# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 041 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
age = int(input('Digite sua idade: '))
print()
if age < 10:
    print('Seu nivel: \033[1;30mMirim\033[m')
elif 15 > age > 9:
    print('Seu nivel: \033[1;36mInfantil\033[m')
elif 20 > age > 14:
    print('Seu nivel: \033[1;35mJunior\033[m')
elif age == 20:
    print('Seu nivel: \033[1;34mSenior\033[m')
else:
    print('Seu nivel: \033[1;31mMaster\033[m')

# ------ Footers ------ #
print(subfooter)
print(footer)