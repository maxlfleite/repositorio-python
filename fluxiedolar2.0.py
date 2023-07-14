print('''
----------------------------------------------------------------
                    Cálculo Fluxie Dollars
----------------------------------------------------------------
''')
fdollars = float(0)
turma = int(input('''Codigo da turma:
[1] Book
[2] Junior [1, 2, 3]
[3] Junior Starters & F&F
Digite o código [1 - 2 - 3]: '''))

presenca = int(input('Quantas aulas o(a) aluno(a) participou: '))
if presenca == 30:
    fdollars = fdollars + 7
fdollars = fdollars + (presenca * 0.5)
if turma == 1:
    homework = float(input('Quantos exercícios foram feitos [CA + CE] X/60? '))
    if homework == 60:
        fdollars = fdollars + 16
    else:
        fdollars = fdollars + (homework * 0.2)
if turma == 2 or turma == 3:
    homework = float(input('Quantos exercícios foram feitos [CA + CE] X/30? '))
    if homework == 30:
        fdollars = fdollars + 16
    else:
        fdollars = fdollars + (homework * 0.4)
compositions = int(input('Quantas compositions o(a) aluno(a) entregou em dia [0/2]? '))
if turma == 1 or turma == 2:
    fdollars = fdollars + (compositions * 4)
if turma == 3:
    fdollars = fdollars + 8
super_rev = int(input("Quantas Super Reviews o(a) aluno(a) participou no semestre? "))
fdollars = fdollars + (super_rev * 5)
ativ_extra = int(input('Quantas atividades extras o aluno participou no semestre? '))
fdollars = fdollars + (ativ_extra * 7)
conv_day = int(input('Quantas conversation days o aluno participou no semestre? '))
fdollars = fdollars + (conv_day * 10)
excursions = int(input('Quantas Excursions o(a) aluno(a) participou no semestre? '))
fdollars = fdollars + (excursions * 15)
nome = str(input('Digite o nome do aluno: '))
print(f'{nome} - F$ {fdollars:.2f}')
