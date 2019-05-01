# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 036 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
valhou = float(input('Digite o valor da casa: R$ '))
valsal = float(input('Digite o valor de seu salario: R$ '))
loahou = int(input('Digite em quantos anos ira financiar: '))
premen = (valhou / (loahou * 12))
if premen <= valsal * 0.30:
    print()
    print('O valor mensal do emprestimo para a casa: R${:.2f}'.format(premen))
else:
    print()
    print('O pedido de emprestimo para financiar a casa foi NEGADO.')
print()
print(str('Agradecemos pela preferencia e volte sempre!'))

# ------ Footers ------ #
print(subfooter)
print(footer)
