# ------ Modules ------ #

# ------ Header & Footers ------ #
header = (' Desafio 014 ')
footer = ('='*68)
subfooter = ('-'*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
cel = float(input('Digite a temperatura em Celsius: '))
print('Tempuratura em Fahrenheit: {}°'.format(float((1.8 * cel) + 32)))

# ------ Footers ------ #
print(subfooter)
print(footer)

