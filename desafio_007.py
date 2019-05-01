# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 002 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
aluno = str(input('Nome do aluno: '))
nota1 = float(input('Nota do primeiro semestre do aluno {}: '.format(aluno)))
nota2 = float(input('Nota do segundo semestre do aluno {}: '.format(aluno)))
print('A media da nota do {}: {}'.format(aluno, float(nota1 + nota2)/2))
print('OR media em 1 digito depois da virgula: {:.1f}'.format(float(nota1 + nota2)/2))
print()

# ------ Footers ------ #
print(subfooter)
print(footer)
