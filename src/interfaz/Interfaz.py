# Importar las librerías necesarias
from matplotlib import pyplot as plt
from modelo.Conjunto import Conjunto

# Definir una función para ejecutar el programa
def execute():
    # Crear dos conjuntos
    A = Conjunto([1, 2, 3, 4, 5])
    B = Conjunto([4, 5, 6, 7, 8])
    C = Conjunto([4, 3, 6, 9, 10])

    # Realizar operaciones en conjuntos
    union = A.union(B)
    elementosA = A.diferencia(B).diferencia(C)
    elementosB = B.diferencia(A).diferencia(C)
    elementosC = C.diferencia(A).diferencia(B)
    elementosAB = A.interseccion(B).diferencia(C)
    elementosBC = B.interseccion(C).diferencia(A)
    elementosAC = A.interseccion(C).diferencia(B)
    interseccion = A.interseccion(B).interseccion(C)
    diferencia = A.diferencia(B)
    complemento = A.complemento(B)

    # Crear una figura para el diagrama de Venn
    venn = plt.figure()
    venn_ax = venn.add_subplot(111)

    # Dibujar los conjuntos
    venn_ax.add_patch(plt.Circle((0.3, 0.6), 0.25, color='blue', alpha=0.5))
    venn_ax.add_patch(plt.Circle((0.7, 0.6), 0.25, color='orange', alpha=0.5))
    venn_ax.add_patch(plt.Circle((0.5, 0.3), 0.25, color='red', alpha=0.5))

    # Agregar los nombres de los conjuntos
    venn_ax.annotate('A', (0.3, 0.6), xytext=(0.1, 0.6), ha='center', va='center')
    venn_ax.annotate('B', (0.7, 0.6), xytext=(0.9, 0.6), ha='center', va='center')
    venn_ax.annotate('C', (0.5, 0.3), xytext=(0.5, 0.1), ha='center', va='center')

    # Agregar elementos de conjuntoA
    for i, elemento in enumerate(elementosA.elementos):
        venn_ax.annotate(str(elemento), (0.25, 0.55), xytext=(0.25, 0.55 + (i+1)*0.05), ha='center', va='center')

    # Agregar elementos de conjuntoB
    for i, elemento in enumerate(elementosB.elementos):
        venn_ax.annotate(str(elemento), (0.75, 0.55), xytext=(0.75, 0.55 + (i+1)*0.05), ha='center', va='center')

    # Agregar elementos de conjuntoC
    for i, elemento in enumerate(elementosC.elementos):
        venn_ax.annotate(str(elemento), (0.5, 0.2), xytext=(0.5, 0.2 + (i+1)*0.05), ha='center', va='center')

    # Agregar elementos del segemento AC
    for i, elemento in enumerate(elementosAC.elementos):
        venn_ax.annotate(str(elemento), (0.38, 0.4), xytext=(0.38, 0.4 + (i+1)*0.05), ha='center', va='center')

    # Agregar elementos del segemento AB
    for i, elemento in enumerate(elementosAB.elementos):
        venn_ax.annotate(str(elemento), (0.5, 0.55), xytext=(0.5, 0.55 + (i+1)*0.05), ha='center', va='center')

    # Agregar elementos del segemento BC
    for i, elemento in enumerate(elementosBC.elementos):
        venn_ax.annotate(str(elemento), (0.63, 0.4), xytext=(0.63, 0.4 + (i+1)*0.05), ha='center', va='center')

    # Agregar elementos de la intersección
    for i, elemento in enumerate(interseccion.elementos):
        venn_ax.annotate(str(elemento), (0.5, 0.45), xytext=(0.5, 0.45 + (i+1)*0.05), ha='center', va='center')

    # Ajustar límites y etiquetas
    venn_ax.set_xlim(0, 1)
    venn_ax.set_ylim(0, 1)
    venn_ax.set_xticks([])
    venn_ax.set_yticks([])
    venn_ax.set_aspect('equal')

    # Mostrar el diagrama
    plt.text(0.5, 0.97, f'Unión: {union}', ha='center', va='center')
    plt.text(0.5, 0.92, f'Diferencia: {diferencia}', ha='center', va='center')
    plt.text(0.5, 0.87, f'Complemento: {complemento}', ha='center', va='center')
    plt.show()
