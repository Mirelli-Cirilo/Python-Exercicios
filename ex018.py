from math import cos, tan, sin, radians
angulo = float(input('Digite o ângulo:'))
print('O valor do seno é {:.2f}°'.format(sin(radians(angulo))))
print('O valor do cosseno é {:.2f}°'.format(cos(radians(angulo))))
print('O valor da tangente é {:.2f}°'.format(tan(radians(angulo))))
