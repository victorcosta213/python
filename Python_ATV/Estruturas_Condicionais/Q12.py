numero_identificacao = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media_exercicios = float(input("Digite a média dos exercícios: "))

media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

if media_aproveitamento >= 90:
    conceito = 'A'
elif media_aproveitamento >= 75:
    conceito = 'B'
elif media_aproveitamento >= 60:
    conceito = 'C'
elif media_aproveitamento >= 40:
    conceito = 'D'
else:
    conceito = 'E'

print(f"Número do aluno: {numero_identificacao}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média dos exercícios: {media_exercicios}")
print(f"Média de aproveitamento: {media_aproveitamento:.2f}")
print(f"Conceito: {conceito}")

if conceito in ['A', 'B', 'C']:
    print("Aprovado")
else:
    print("Reprovado")
