nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ")
estado_civil = input("Digite o estado civil (CASADA/SOLTEIRA): ")

if sexo.upper() == "F" and estado_civil.upper() == "CASADA":
    tempo_casada = int(input("Digite o tempo de casada (anos): "))
    print(f"{nome} é casada há {tempo_casada} anos.")
