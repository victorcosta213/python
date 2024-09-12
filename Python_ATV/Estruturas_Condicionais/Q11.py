preco_etiqueta = float(input("Digite o preço normal de etiqueta: "))
codigo_pagamento = int(input("Digite o código de pagamento (1 a 4): "))

if codigo_pagamento == 1:
    valor_final = preco_etiqueta * 0.90 
elif codigo_pagamento == 2:
    valor_final = preco_etiqueta * 0.85 
elif codigo_pagamento == 3:
    valor_final = preco_etiqueta  
elif codigo_pagamento == 4:
    valor_final = preco_etiqueta * 1.10  
else:
    valor_final = preco_etiqueta
    print("Código de pagamento inválido.")

print(f"Valor a ser pago: R$ {valor_final:.2f}")


