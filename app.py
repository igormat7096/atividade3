# entrada de dados 
print(" Trem fantasma ")
nome = input("Informe o seu nome: ")
idade = int(input("informe a sua Idade: "))
peso = float(input("informe o seu Peso em KG: ").replace(",","."))


# verifica a idade do usuário
print(f"{idade} Liberado. " if idade >= 10 else f"{idade} Bloqueado")
print(f"{peso} Liberado. " if peso <= 150 else f"{peso} Bloqueado")

