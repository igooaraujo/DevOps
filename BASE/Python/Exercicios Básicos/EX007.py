v1 = float(input('QUAL A VELOCIDADE DO CARRO: '))
if v1 > 80:
    print('NÃO ULTRAPASSOU O LIMITE!')
    m = v1-80
    m1 = m*7
    print('VOCÊ FOI MULTADO E TERÁ QUE PAGAR UMA MULTA DE {}'.format(m1))
print('VOCE ESTÁ DENTRO DO LIMITE DE VELOCIDADE')


