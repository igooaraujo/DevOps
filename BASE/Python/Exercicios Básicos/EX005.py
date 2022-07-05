import math
N1 = float(input('DIGITE O CATETO OPOSTO: '))
N2 = float(input('DIGITE O CATE ADJACENTE: '))
N3 = math.hypot(N1, N2)
print('O COMPRIMENTO DA HIPOTENUSA É: {:.2f}'.format(N3))

