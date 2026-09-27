alfaM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfam = 'abcdefghojklmnopqrstuvwxyz'

l = input()

if l in alfaM:
    print(alfaM.index(l)+1)
else:
    print(alfam.index(l)+1)
