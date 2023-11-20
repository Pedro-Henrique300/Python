#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Elabore um programa que calcule o valor a ser pago por um produto, 
   considerando o seu preço normal e condição de pagamento:
   
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''



valor_compra = float(input('Preço das compras: R$'))

print('''\nFORMAS DE PAGAMENTO:
Tecle [1] para pagar à vista dinheiro/cheque com 10% de desconto
Tecle [2] para pagar à vista no cartão com 5% de desconto
Tecle [3] para pagar em até 2x no cartão: preço formal
Tecle [4] para pagar em 3x ou mais no cartão: 20% de juros''')



condicao_pagamento = int(input('\nDigite sua resposta aqui: '))




if condicao_pagamento == 1:
    total = valor_compra - (valor_compra * 10 / 100)
    
elif condicao_pagamento == 2:
    total = valor_compra - (valor_compra * 5 / 100)
          
elif condicao_pagamento == 3:
    total = valor_compra
    parcela = valor_compra / 2
    print(f'\nSua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS!')
          
elif condicao_pagamento == 4:
    total = valor_compra + (valor_compra * 20 / 100)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print(f'\nSua compra será parcelada em {total_parcelas}x de R${parcela:.2f} COM JUROS!')

else:
    valor_compra = 0
    total = 0
    print('\n\033[1;31mOpção Invalida!\033[m Tente novamente')

print(f'Sua compra de R${valor_compra:.2f} vai custar R${total:.2f} no final')

