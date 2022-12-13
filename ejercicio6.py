import numpy as np

def pedir_numero():
    while True:
        try:
            n = int(input("Introduce un número para determinar el orden de la matriz: "))
            return n
        except ValueError:
            print("Error. Introduce un número entero")

def matriz(n):
    return np.random.randint(1, 100, size=(n, n))

def rotar_clockwise(matriz):
    return np.rot90(matriz)

def rotar_anticlockwise(matriz):
    matrix1 = np.rot90(matriz)
    matrix2 = np.rot90(matrix1)
    matrix3 = np.rot90(matrix2)
    return matrix3

def main():
    n = pedir_numero()
    matrix = matriz(n)
    print(matrix, '\n')
    print(rotar_clockwise(matrix), '\n')
    print(rotar_anticlockwise(matrix))

if __name__ == '__main__':
    main()