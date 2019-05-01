# ------ Modules ------ #
from math import radians, sin, cos, tan

# ------ Header & Footers ------ #
header = (' Desafio 018 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
ang = float((input('Digite o grau de um agulo: ')))
print()
sena = float(sin(radians(ang)))
cosa = float(cos(radians(ang)))
tana = float(tan(radians(ang)))
print('O seno do angulo {}° = {:.2f}°'.format(ang, sena))
print('O coseno do angulo {}° = {:.2f}°'.format(ang, cosa))
print('A tangente do angulo {}° = {:.2f}°'.format(ang, tana))

# ------ Footers ------ #
print(subfooter)
print(footer)

