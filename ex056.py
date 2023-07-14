'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo,
qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.'''
frase = '| People Analizator Tabajara |'
print("-"*len(frase))
print(frase)
print("-"*len(frase))
somaidade = int(0)
homemvelho = 'abc'
idadehvelho = int(0)
countmulher20 = int(0)
for c in range (1, 5):
    print(f"------- {c}ª PESSOA -------")
    nome = str(input(f"Digite o nome do {c}º cidadão: "))
    idade = int(input("Digite a idade do mesmo: "))
    somaidade = somaidade + idade
    sexo = str(input("Digite o sexo do mesmo [M/F]: ")).upper()
    if (sexo == 'M'):
        if idade > idadehvelho:
            idadehvelho = idade
            homemvelho = nome
    if (sexo == 'F'):
        if idade < 20:
            countmulher20 = countmulher20 + 1
media = float(somaidade / 4)
print(f"Média de idade do grupo: {media:.1f}")
print(f"O homem mais velho cadastrado foi {homemvelho} com a idade de {idadehvelho} anos.")
print(f"Foram cadastradas {countmulher20} mulheres com a idade inferior a 20 anos.")


