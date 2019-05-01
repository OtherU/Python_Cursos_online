# ------ Modules ------ #
from time import sleep

# ------ Header & Footers ------ #
header = str(' \033[1;32mDesafio 065\033[m ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
print(str('Numeros pares de 1 a 50.'))
print(subfooter)
for nmb in range(2, 50+1, 2):
    print(nmb, end=' ')
print()
print("That was easy, doesn't it?")

# ------ Footers ------ #
print(subfooter)
print(footer)