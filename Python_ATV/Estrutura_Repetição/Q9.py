A = float(input("Digite o valor inicial (A) da sequência em P.G.: "))
R = float(input("Digite a razão (R) da sequência em P.G.: "))
for i in range(10):
    valor = A * (R ** i)
    print(valor)
