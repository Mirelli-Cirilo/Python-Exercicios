preco = float(input('Digite o preço atual:'))
desconto = preco - (5/100) * preco
print('o produto custava {:.2f} e agora com desconto de 5% custa {:.2f}.'.format(preco, desconto))
