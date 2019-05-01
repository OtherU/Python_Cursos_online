# ------ Modules ------ #

# ------ Header & Footers ------ #
header = str(' Desafio 037 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
n1 = int(input('Digite um numero: '))
print(str('''Choose a type conversion bellow!
[ 1 ] Convert to binary.
[ 2 ] Convert to octal.
[ 3 ] Convert to hexadecimal.'''))
opt = int(input('Digite o tipo para conversion: '))
if opt == 1:
    print()
    print('The value {} in binary: {}'.format(n1, bin(n1)[2:]))
elif opt == 2:
    print()
    print('The value {} in octal: {}'.format(n1, oct(n1)[2:]))
elif opt == 3:
    print()
    print('The value {} in hexadecimal: {}'.format(n1, hex(n1)[2:]))
else:
    print()
    print('Value invalid, unable values: opt [1] or [2] or [3]')

# ------ Footers ------ #
print(subfooter)
print(footer)
