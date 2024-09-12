sexo = input("Digite o sexo (M/F): ")
altura = float(input("Digite a altura (em metros): "))

if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7

print(f"Peso ideal: {peso_ideal:.2f} kg")
