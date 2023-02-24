print('{:-^50}'.format('LOJAS BRASILEIRAS'))
preco = float(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção?'))
tot = 0
if opcao == 1:
    total = preco - (10 / 100 * preco)
    tot = total
elif opcao == 2:
    total = preco - (5 / 100 * preco)
    tot = total
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcela em 2x de {:.2f}'.format(parcela))
    tot = total
elif opcao == 4:
    total = preco + (20 / 100 * preco)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc, parcela))
    tot = total
else:
    print('Escolha inválida')
print('Sua compra de {:.2f} vai custar {:.2f}'.format(preco, tot))
