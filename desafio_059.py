# ------ Modules ------ #
from time import sleep

# ------ Header & Footers ------ #
header = str(' Desafio 059 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
nmb1 = int(input('Digite um numero: '))
nmb2 = int(input('Digite um numero: '))
chse = 0

print()
print(str('''Escolha uma opcao abaixo!\n
----------------------------
 [ 1 ] Somar
 [ 2 ] Multiplicar
 [ 3 ] Comparar
 [ 4 ] Novos numeros
 [ 5 ] Sair do programa
----------------------------	'''))
while chse != "5":
    chse = input('Escolha uma opcao acima: ')
    if chse == "1":
        # Testing SUM Function!
        print('Expressao:\n{} + {}= {}'.format(nmb1, nmb2, nmb1 + nmb2))
        print()
        print('-' * 20)
    elif chse == "2":
        # Testing Multiplication Function!
        print('Expressao:\n{} x {}= {}'.format(nmb1, nmb2, nmb1 * nmb2))
        print()
        print('-' * 20)
    elif chse == "3":
        if nmb1 > nmb2:
            print('O maior numero entre {} e {}: {}'.format(nmb1, nmb2, nmb1))
            print()
            print('-' * 20)
        elif nmb2 > nmb1:
            print('O maior numero entre {} e {}: {}'.format(nmb1, nmb2, nmb2))
            print()
            print('-' * 20)
        else:
            print('Os numeros {} e {} sao iguais!'.format(nmb1, nmb2))
            print()
            print('-' * 20)
    elif chse == "4":
        print('Processing...')
        for i in range(1, 3):
            print('-', end='')
            sleep(1)
        print('>')
        print()
        print('Analizando Novos Numeros!')
        nmb1 = int(input('Digite um numero: '))
        nmb2 = int(input('Digite um numero: '))
        print()
    elif chse == "5":
        for procss in range(1, 3):
            sleep(0.3)
            print('.', end='')
    else:
        print('Option invalid!\nChoose one[ 1 | 2 | 3 | 4 | 5 ]')
        print()
print('Saindo do programa')

# ------ Footers ------ #
print(subfooter)
print(footer)
