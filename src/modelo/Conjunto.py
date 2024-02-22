import matplotlib.pyplot as plt
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

# Crear dos conjuntos
A = Conjunto([1, 2, 3, 4, 5])
B = Conjunto([4, 5, 6, 7, 8])

# Realizar operaciones en conjuntos
union = A.union(B)
interseccion = A.interseccion(B)
diferencia = A.diferencia(B)
complemento = A.complemento(B)

# Mostrar los resultados en una interfaz gráfica
fig, ax = plt.subplots(figsize=(6, 6))
venn2([set(A.elementos), set(B.elementos)], set_labels=('A', 'B'))
plt.title('Diagrama de Venn')
plt.show()
