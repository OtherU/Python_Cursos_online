# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 040 ')
subfooter = str('-'*68)
footer = str('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
note1 = float(input('Digite a primeira nota: '))
note2 = float(input('Digite a segunda nota: '))
med = float(note1 + note2) / 2
if med < 5.0:
    print()
    print('Sua media final foi {:.2f}, voce foi \033[1;31mREPROVADO\033[m'.format(med))
elif 7 > med >= 5.0:
    print()
    print('A sua media foi {:.2f}, voce esta de \033[4;33mRECUPERACAO\033[m'.format(med))
    print('''* You can write like:
med > 5.0 and med <= 6.9 \033[1;31mOR\033[m  7 > med >=5((med is minor than 7 
AND med is major or equal 5))''')
elif med >= 7.0:
    print()
    print('Sua media foi {:.2f}, voce foi \033[1;34mAPROVADO\033[m, Parabens!!!')

# ------ Footers ------ #
print(subfooter)
print(footer)
