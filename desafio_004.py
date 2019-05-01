# ------ Modules ------ #


# ------ Header & Footers ------ #
header = str(' Desafio 004 ')
subheader1 = str('1.Testing primitives types!')
subheader2 = str('2.Testing primitive for int!')
subheader3 = str('3.Testing primitive for float!')
subheader4 = str('4.Testing primitive for bool!')
subheader5 = str('5.Testing is* for tests for another values!')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Sub-Header1 ------ #
print('{:-^68}'.format(subheader1))

# ------ Body1 ------ #
value0 = str(input('Testing primitive for string(default): '))
print(type(value0))
print(value0)
print(subfooter)

# ------ Sub-Header2 ------ #
print('{:-^68}'.format(subheader2))

# ------ Body2 ------ #
value1 = int(input('Digite a number: '))
print(type(value1))
print(value1)
print(subfooter)

# ------ Sub-Header3 ------ #
print('{:-^68}'.format(subheader3))

# ------ Body3 ------ #
value2 = float(input('Digite a number: '))
print(type(value2))
print(value2)
print(subfooter)

# ------ Sub-Header4 ------ #
print('{:-^68}'.format(subheader4))

# ------ Body4 ------ #
value3 = bool(input('Digite um numero: '))
print(type(value3))
print(value3)
print(subfooter)

# ------ Sub-Header5 ------ #
print('{:-^68}'.format(subheader5))

# ------ Body5 ------ #
value4 = input('Digite a anything: ')
print('Is it a numeric case?', value4.isnumeric())
print('Is it a alphanumber case?', value4.isalnum())
print('Is it a decimal case?', value4.isdecimal())
print('Is it a digital case?', value4.isdigit())
print('Is it a title case?', value4.istitle())
print('Is it a identifier case?', value4.isidentifier())
print('Is it a lowercase case?', value4.islower())
print('Is it a printable case?', value4.isprintable())

# ------ Footers ------ #
print(subfooter)
print(footer)