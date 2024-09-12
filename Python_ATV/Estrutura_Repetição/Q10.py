A = int(input("Digite um valor para calcular o fatorial (A!): "))
fatorial = 1
for i in range(1, A + 1):
    fatorial *= i
print(f"{A}! = {fatorial}")
