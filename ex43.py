peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso / (altura ** 2)
print('O valor do seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif (imc >= 18.5) and (imc < 25):
    print('Você está no peso ideal!')
elif (imc >= 25) and (imc < 30):
    print('SOBREPESO!')
elif (imc >= 30) and (imc < 40):
    print('OBESIDADE')
elif imc > 40:
    print('OBESIDADE MÓRBIDA')
