A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))

valores = [A, B, C]
valores.sort(reverse=True)

print("Valores em ordem decrescente:", valores)
