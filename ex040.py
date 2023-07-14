'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''
frase = 'Media Calculator Tabajara'
print(frase)
print('=' * len(frase))
nota1 = float(input("Primeira Nota: "))
nota2 = float(input("Segunda Nota: "))
media = (nota1 + nota2) / 2
print("Média: {:.1f}".format(media))
if media < 5.0:
    print("Bicho burro da porra. Essa desgraça é bolsonarista, só pode! REPROVADO!!!")
elif (media >= 5.0 and media < 7):
    print("Esse é preguiçoso! Precisa se dedicar um pouco mais. RECUPERAÇÃO.")
elif (media >= 7):
    print("Não fez mais que sua obrigação. APROVADO.")
