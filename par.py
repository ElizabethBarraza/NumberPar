def es_par(n):
    """Regresa True si n es par, False si es impar."""
    if not isinstance(n, int):
        raise TypeError("Debe ser un entero")
    return n % 2 == 0


if __name__ == "__main__":
    dato = input("Ingresa un número: ")
    try:
        num = int(dato)
        if es_par(num):
            print("Es par")
        else:
            print("No es par")
    except ValueError:
        print("Error: debes escribir un número entero")