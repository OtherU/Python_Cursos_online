# ------ Modules ------ #
# ------ Header & Footers ------ #
header = str(' Desafio 056 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
mjage = 0
mnagect = 0
mdrqage = 0
oldmnme = ''
for lp in range(1, 5):
    rqname = input('Digite seu nome: ')
    rqage = int(input('Digite sua idade: '))
    rqsex = input('Digite seu sexo(M/F): ')
    mdrqage += rqage
    print()
    if lp == "1":
        mjage = rqage
    else:
        if rqage >= mjage and rqsex == 'M':
            mjage = rqage
            oldmnme = rqname
        elif rqage <= 21 and rqsex == 'F':
            mnagect += 1
print('Analisando Informacoes...')
print(' Media Da Idade Do Grupo: {:.0f} anos'.format(mdrqage / 4))
# You also can round numbers using "round(NUMBERS)" function as bellow!
#print(' Media Da Idade Do Grupo: {} anos'.format(round(mdrqage / 4)))
print()
print('Genero Masculino mais velho do grupo:')
print(' NOME= {}\n IDADE= {}'.format(oldmnme, mjage))
print()
print('Mulheres de menor de idade do grupo: {}'.format(mnagect))

# ------ Footers ------ #
print(subfooter)
print(footer)
