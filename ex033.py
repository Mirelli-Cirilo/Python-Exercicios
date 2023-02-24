a = int(input('Digite um número entre 0 e 10:'))
b = int(input('Digite outro número entre 0 e 10'))
c = int(input('Digite o último número:'))
# verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é o maior
maior = b
if a > b and a > c:
    maior = a
if c > a and c > b:
    maior = c
print(f'\033[1;33mO maior valor digitado foi {maior}\033[m')
print(f'\033[1;31mO menor valor digitado foi {menor}\033[m')
