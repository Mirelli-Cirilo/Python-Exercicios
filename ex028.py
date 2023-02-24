from random import randint
from time import sleep
aleatorio = randint(0, 5)
print('#' * 10)
print('Adivinhe o número que estou pensando...')
print('#' * 10)
chute = int(input('Chute um número entre 0 e 5:'))
print('Pensando...')
sleep(2)
if chute < aleatorio:
    print(f'Chutou baixo! Eu pensei no número {aleatorio}')
elif chute > aleatorio:
    print(f'Chutou alto! Eu pensei no número {aleatorio}')
else:
    print('Parabénssss, acertou')
