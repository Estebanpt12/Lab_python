import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

class Conjunto:
    def __init__(self, elementos):
        self.elementos = elementos

    def union(self, otro_conjunto):
        resultado = self.elementos.copy()
        for elemento in otro_conjunto.elementos:
            if elemento not in resultado:
                resultado.append(elemento)
        return Conjunto(resultado)

    def interseccion(self, otro_conjunto):
        resultado = []
        for elemento in self.elementos:
            if elemento in otro_conjunto.elementos:
                resultado.append(elemento)
        return Conjunto(resultado)

    def diferencia(self, otro_conjunto):
        resultado = []
        for elemento in self.elementos:
            if elemento not in otro_conjunto.elementos:
                resultado.append(elemento)
        return Conjunto(resultado)

    def complemento(self, *otros_conjuntos):
        resultado = []
        for otro_conjunto in otros_conjuntos:
            for elemento in otro_conjunto.elementos:
                if elemento not in self.elementos and elemento not in resultado:
                    resultado.append(elemento)
        return Conjunto(resultado)

    def __str__(self):
        return str(self.elementos)

def main():
    # Crear dos conjuntos
    A = Conjunto([1, 2, 3, 4, 5])
    B = Conjunto([4, 5, 6, 7, 8])

    # Realizar operaciones en conjuntos
    union = A.union(B)
    interseccion = A.interseccion(B)
    diferencia = A.diferencia(B)
    complemento = A.complemento(B)

    venn = plt.figure()
    venn_ax = venn.add_subplot(111)

    # Dibujar los conjuntos
    venn_ax.add_patch(plt.Circle((0.3, 0.5), 0.3, color='blue', alpha=0.5))
    venn_ax.add_patch(plt.Circle((0.7, 0.5), 0.3, color='orange', alpha=0.5))

    # Agregar elementos de conjunto1
    for i, elemento in enumerate(diferencia.elementos):
        venn_ax.annotate(str(elemento), (0.3, 0.5), xytext=(0.3, 0.5 + (i+1)*0.05), ha='center', va='center')

    # Agregar elementos de conjunto2
    for i, elemento in enumerate(complemento.elementos):
        venn_ax.annotate(str(elemento), (0.7, 0.5), xytext=(0.7, 0.5 + (i+1)*0.05), ha='center', va='center')

    # Dibujar la intersección
    venn_ax.add_patch(plt.Circle((0.5, 0.5), 0.3, color='green', alpha=0.5))

    # Agregar elementos de la intersección
    for i, elemento in enumerate(interseccion.elementos):
        venn_ax.annotate(str(elemento), (0.5, 0.5), xytext=(0.5, 0.5 + (i+1)*0.05), ha='center', va='center')

    # Ajustar límites y etiquetas
    venn_ax.set_xlim(0, 1)
    venn_ax.set_ylim(0, 1)
    venn_ax.set_xticks([])
    venn_ax.set_yticks([])
    venn_ax.set_aspect('equal')

    # Mostrar el diagrama
    plt.show()

if __name__ == "__main__":
    main()
