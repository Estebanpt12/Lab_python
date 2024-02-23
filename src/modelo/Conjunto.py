class Conjunto:
    def __init__(self, elementos):
        # Inicializa la clase Conjunto con una lista de elementos
        self.elementos = elementos

    def union(self, otro_conjunto):
        # Realiza la operación de unión entre dos conjuntos
        # Crea una lista resultado con los elementos del primer conjunto
        resultado = self.elementos.copy()
        # Itera sobre los elementos del segundo conjunto
        for elemento in otro_conjunto.elementos:
            # Si el elemento no está en la lista resultado, lo agrega
            if elemento not in resultado:
                resultado.append(elemento)
        # Retorna un nuevo objeto Conjunto con la lista resultado
        return Conjunto(resultado)

    def interseccion(self, otro_conjunto):
        # Realiza la operación de intersección entre dos conjuntos
        # Crea una lista resultado vacía
        resultado = []
        # Itera sobre los elementos del primer conjunto
        for elemento in self.elementos:
            # Si el elemento está en el segundo conjunto, lo agrega a la lista resultado
            if elemento in otro_conjunto.elementos:
                resultado.append(elemento)
        # Retorna un nuevo objeto Conjunto con la lista resultado
        return Conjunto(resultado)

    def diferencia(self, otro_conjunto):
        # Realiza la operación de diferencia entre dos conjuntos
        # Crea una lista resultado vacía
        resultado = []
        # Itera sobre los elementos del primer conjunto
        for elemento in self.elementos:
            # Si el elemento no está en el segundo conjunto, lo agrega a la lista resultado
            if elemento not in otro_conjunto.elementos:
                resultado.append(elemento)
        # Retorna un nuevo objeto Conjunto con la lista resultado
        return Conjunto(resultado)

    def complemento(self, *otros_conjuntos):
        # Realiza la operación de complemento entre conjuntos
        # Crea una lista resultado vacía
        resultado = []
        # Itera sobre los conjuntos adicionales
        for otro_conjunto in otros_conjuntos:
            # Itera sobre los elementos del conjunto adicional
            for elemento in otro_conjunto.elementos:
                # Si el elemento no está en el primer conjunto y no está en la lista resultado, lo agrega
                if elemento not in self.elementos and elemento not in resultado:
                    resultado.append(elemento)
        # Retorna un nuevo objeto Conjunto con la lista resultado
        return Conjunto(resultado)

    def __str__(self):
        # Retorna una representación en cadena de los elementos del conjunto
        return str(self.elementos)
