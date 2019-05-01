# ------ Modules ------ #
# ------ Header & Footers ------ #
header = str(' Desafio 053 ')
subfooter = ('-' * 68)
footer = ('=' * 68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
phrase = input('Digite uma frase: ').strip().upper()
sptphrase = phrase.split()
jnphrase = ''.join(sptphrase)
print()
print(subfooter)
print('Invert the order using for statment!')
ivrphrase = ''
for letr in range(len(jnphrase) - 1, - 1, - 1):
    ivrphrase += jnphrase[letr]
print(ivrphrase)
print(subfooter)
print("Invert the order using Python's function")
ivtifphrs = jnphrase[::-1]
print(ivtifphrs)
if jnphrase == ivrphrase or ivtifphrs:
    print('A frase {} e uma frase Polidromo!'.format(phrase))
else:
    print('A frase "{}" \033[1;31mNAO\033[m e uma frase Polidromo!'.format(phrase))

# ------ Footers ------ #
print(subfooter)
print(footer)
