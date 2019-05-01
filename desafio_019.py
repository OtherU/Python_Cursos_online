# ------ Modules ------ #
from random import choice

# ------ Header & Footers ------ #
header = (' Desafio 019 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
aluno1 = "Allen"
aluno2 = "Nick"
aluno3 = "Monroe"
aluno4 = "Adline"
print('Alunos que poderam ser escolhidos: {}, {}, {}, {}'.format(aluno1, aluno2, aluno3, aluno4))
print()
print('O aluno escolhido sera: {}'.format(choice([aluno1, aluno2, aluno3, aluno4])))

# ------ Footers ------ #
print(subfooter)
print(footer)
