soma_valores = 0
soma_valores_pares=0
quantidade_valores = 0
quantidade_pares = 0
quantidade_impares = 0


while True:
    try:
        numero = float(input("Digite um número (ou zero para encerrar): "))
        if numero == 0:
            break 
        elif numero > 0:
            soma_valores += numero
            quantidade_valores += 1
            if numero % 2 == 0:
                quantidade_pares += 1
                soma_valores_pares += numero
            else:
                quantidade_impares += 1
        else:
            print("Número inválido. Digite um número positivo ou zero.")
    except ValueError:
        print("Valor inválido. Digite um número válido.")


if quantidade_valores > 0:
    media_geral = soma_valores / quantidade_valores
    media_pares = soma_valores_pares / quantidade_pares
else:
    media_geral = 0
    media_pares = 0


print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Média dos valores pares: {media_pares:.2f}")
print(f"Média geral dos números lidos: {media_geral:.2f}")
