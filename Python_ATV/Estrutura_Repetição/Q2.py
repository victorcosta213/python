num = 0
altura = []


while num != 15:
    altura.append(float(input("Didite a altura: ")))
    num +=1

maior = altura[1]
menor = altura[1]

for i in altura:
    if i>maior:
        maior=i
    elif i<menor:
        menor = i


print("A maior altura: "+str(maior)+"m")
print("A menor altura: "+str(menor)+"m")


