# ------ Modules ------ #
from math import pow, sqrt

# ------ Header & Footers ------ #
header = (' Desafio 017 ')
footer = ('='*68)
subfooter = ('-'*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
coca = ((pow(co, 2)) + (pow(ca, 2)))
print('O valor da hipotenusa e: {}'.format(int(sqrt(coca))))

# ------ Footers ------ #
print(subfooter)
print(footer)







