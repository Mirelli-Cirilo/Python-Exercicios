from datetime import date
atual = date.today().year
sexo = str(input('sexo feminino ou masculino?'))
if sexo == 'feminino':
    print('Seu alistamento NÂO é obrigatório')
if sexo == 'masculino':
    print('Seu alistamento É obrigatório')
ano = int(input('Digite o seu ano de nascimento:'))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não chegou aos 18, faltam {} ano para seu alistamento'.format(saldo))
    ano = atual + saldo
    print('O ano do seu alistamento será {}'.format(ano))
else:
    saldo = idade - 18
    print(f'Você deveria ter se alistado {saldo} anos atrás')
    ano = atual - saldo
    print('O ano do seu alistamento foi {}'.format(ano))
