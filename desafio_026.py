# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 026 ')
subfooter = str('-'*68)
footer = str('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
phse = str(input('Digite um frase: '))
phsesp = phse.split()
print()
print('1. A letra "a" aparece {} vezes na frase acima.'.format(phse.count('a')))
print('2. A primeira vez em que a letra "a" aparece e na posicao {}.'.format(phse[0:].find('a')))
print('3. A ultima vez em que a letra "a" aparece e na posicao {}.'.format(phse[::].rfind('a')))

# ------ Footers ------ #
print(subfooter)
print(footer)

