casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salário?'))
anos = int(input('Em quantos anos pagará a casa?'))
preco = casa / (anos * 12)
negado = (30/100 * salario)
if preco >= negado:
    print('O seu empréstimo foi negado!')
else:
    print('\033[1;32;40mo valor a ser pago será {:.2f}\033[m'.format(preco))
