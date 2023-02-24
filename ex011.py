larg = float(input('Digite a largura em metros:'))
alt = float(input('Também a altura:'))
area = larg * alt
print('Sua dimensão é de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede você vai precisar de {} litros de tinta!'.format(tinta))

