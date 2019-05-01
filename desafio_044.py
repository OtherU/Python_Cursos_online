# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 044 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
prod = float(input('Digite o valor do produto:R$ '))
print('''Escolha sua forma de pagamento.
  1. CASH
  2. CHEQUE
  3. CREDIT CARD''')
opmg = int(input('Digite o numero da opcao desejada: '))
print()
if opmg == 1 or opmg == 2:
    val1 = prod - (prod * 0.10)
    print('O valor Total sera:R$ {:.2f}'.format(val1))
elif opmg == 3:
    print('''Escolha sua forma de pagamento: 
    1. A VISTA
    2. PARCELAR''')
    opmg2 = int(input('Digite o numero da opcao desejada: '))
    if opmg2 == 1:
        val2 = prod - (prod * 0.05)
        print('O valor Total sera:R$ \033[1;34m{:.2f}\033[m'.format(val2))
    elif opmg2 == 2:
        parc = int(input('Digite em quantas vezes sera parcelado: '))
        if parc < 3:
            print(input('O valor Total sera:R$ \033[1;34m{:.2f}\033[m'.format(prod)))
        else:
            val3 = prod + (prod * 0.20)
            print('O valor Total sera:R$ \033[1;34m{:.2f}\033[m'.format(val3))
    else:
        print('\033[1;31mNumero incorreto\033[m, tente novamente!')
else:
    print('\033[1;31mNumero incorreto\033[m, tente novamente!')

# ------ Footers ------ #
print(subfooter)
print(footer)
