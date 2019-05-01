# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 033 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
#===========MENOR==============
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
#------------------------------
if n3 < n1 and n3 < n2:
    menor = n3
#============MAIOR=============
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
#------------------------------
if n3 > n1 and n3 > n2:
    maior = n3
#==============================
print()
print('O MENOR numero digitado e: {:.2f}'.format(menor))
print('O MAIOR numero digitado e: {:.2f}'.format(maior))

# ------ Footers ------ #
print(subfooter)
print(footer)
