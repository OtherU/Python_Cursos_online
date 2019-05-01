# ------ Modules ------ #
# ------ Header & Footers ------ #
header = str(' Desafio 055 ')
subfooter = ('-'*68)
footer = ('='*68)

# ------ Header ------ #
print('{:=^68}'.format(header))

# ------ Body ------ #
mnwnm = ''
mjwnm = ''
mjrwghs = 0
mnrwghs = 0
for ppl in range(1, 5):
    name = input('Digite seu nome: ')
    reqwgh = float(input('Digite seu peso: '))
    print()
    if ppl == 1:
        mjrwghs = ppl
        mnrwghs = reqwgh
    else:
        if reqwgh >= mjrwghs:
            mjrwghs = reqwgh
            mjwnm = name
        if reqwgh <= mnrwghs:
            mnrwghs = reqwgh
            mnwnm = name
print("The hottest girl's name is {} and she weighs {}Kg, WOW!".format(mnwnm, mnrwghs))
print("The chubby one's name is {} and she weighs {}Kg!".format(mjwnm, mjrwghs))

# ------ Footers ------ #
print(subfooter)
print(footer)