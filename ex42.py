l1 = float(input('Digite o primeiro comprimento:'))
l2 = float(input('Digite o segundo número:'))
l3 = float(input('Digite o terceiro'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segementos acima formam um triângulo!')
    if l1 == l2 == l3:
        print('EQUILATERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos não formam triângulo!')
