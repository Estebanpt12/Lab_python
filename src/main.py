from interfaz.Interfaz import crear_interfaz
from modelo.Conjunto import Conjunto

def tomar_datos(nombre_conjunto: str):
    return Conjunto(input("Ingresa los elementos del conjunto " + nombre_conjunto +
                          " separados por comas: ").split(','))

if __name__ == "__main__":
    A = tomar_datos("A")
    B = tomar_datos("B")
    C = tomar_datos("C")
    crear_interfaz(A, B, C)

