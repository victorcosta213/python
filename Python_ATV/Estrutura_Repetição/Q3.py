soma_valores = 0
quantidade_valores = 0
quantidade_positivos = 0
quantidade_negativos = 0


while True:
    try:
        valor = float(input("Digite um valor (ou 0 para encerrar): "))
        if valor == 0:
            break 
        soma_valores += valor
        quantidade_valores += 1
        if valor > 0:
            quantidade_positivos += 1
        elif valor < 0:
            quantidade_negativos += 1
    except ValueError:
        print("Valor inválido. Digite um número válido.")


if quantidade_valores > 0:
    media = soma_valores / quantidade_valores
else:
    media = 0


total_valores = quantidade_positivos + quantidade_negativos
if total_valores > 0:
    percentual_positivos = (quantidade_positivos / total_valores) * 100
    percentual_negativos = (quantidade_negativos / total_valores) * 100
else:
    percentual_positivos = 0
    percentual_negativos = 0


print(f"Média aritmética dos valores: {media:.2f}")
print(f"Quantidade de valores positivos: {quantidade_positivos}")
print(f"Quantidade de valores negativos: {quantidade_negativos}")
print(f"Percentual de valores positivos: {percentual_positivos:.2f}%")
print(f"Percentual de valores negativos: {percentual_negativos:.2f}%")
 