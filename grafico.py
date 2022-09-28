import matplotlib.pyplot as plt
from random import randrange

randrange(0,11)

notas_matematica = []
notas_portugues = []
notas_quimica = []
notas_semestre = [notas_matematica, notas_portugues, notas_quimica]
materias = ['Matemática','Português','Química']

for notas in range(8):
    notas_matematica.append(randrange(0,11))
    notas_portugues.append(randrange(0,11))
    notas_quimica.append(randrange(0,11))

i = -1
for materia in notas_semestre:
    i += 1
    x = list(range(1, 9))
    y = materia
    plt.plot(x, y, marker='o')
    plt.title(f'{materias[i]}')
    plt.xlabel('Provas')
    plt.ylabel('Notas')
    plt.show()
