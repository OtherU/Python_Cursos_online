# ------ Modules ------ #
from random import randint
from time import sleep

# ------ Header & Footers VARs ------ #
header = str(' Desafio 045 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print(header.center(68, '='))

# ------ Body ------ #
lsjo = ('rock', 'paper', 'scissors')
pctk = randint(0, 2)
print('''JAN-KEN-PO GAME!!!
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 ] SCISSORS''')
plyr = int(input('Escolha uma opcao acima: '))
if plyr <= 2:
  print('GAME starting...')
  print()
  print('\033[1;32mJAN-...\033[m')
  sleep(1)
  print('\033[1;36m...KEN-...\033[m')
  sleep(1)
  print('\033[1;31m...PO!\033[m')
  sleep(1)
  print('=\033[1;35m■\033[m'*10)
  print('PC chose: {}'.format(lsjo[pctk]))
  print('Player chose: {}'.format(lsjo[plyr]))
  print()
  if pctk == 0:
      if plyr == 0:
          print('Result: \033[1;33mDRAW GAME!\033[m')
      elif  plyr == 1:
          print('Result: \033[1;34mYou WIN!\033[m')
      else:
          print('Result: \033[1;31mYou LOSE!\033[m')
  elif pctk == 1:
      if plyr == 0:
          print('Result: \033[1;31mYou LOSE!\033[m')
      elif plyr == 1:
          print('Result: \033[1;33mDRAW GAME!\033[m')
      else:
          print('Result: \033[1;34mYou WIN!\033[m')
  elif pctk == 2:
      if plyr == 0:
          print('Result: \033[1;34mYou WIN!\033[m')
      elif plyr == 1:
          print('Result: \033[1;31mYou LOSE!\033[m')
      else:
          print('Result: \033[1;33mDRAW GAME!\033[m')
else:
 print('option \033[1;31mINVALID\033[m')
print('=\033[1;35m■\033[m'*10)

# ------ Footers ------ #
print(subfooter)
print(footer)
