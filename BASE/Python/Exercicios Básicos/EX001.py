algo = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(algo))
print('É um número? ', algo.isnumeric())
print('É uma palavra ', algo.isalpha())
print('Tem espaços ', algo.isspace())
print('Tem letras maiusculas ', algo.isupper())
print('Tem letras minusculas ', algo.islower())
print('É alfanumérico ', algo.isalnum())
print('Esta capitalizada ', algo.istitle())
