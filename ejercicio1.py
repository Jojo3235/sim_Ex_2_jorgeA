def separar_kword(palabra):
    palabra2 = palabra.split('#')
    return palabra2

def sacar_mensaje(palabra):
    for elemento in palabra:
        if len(palabra) == 2:
            return palabra[-1]
        else: 
            return 'No se pueden introducir # en medio del mensaje'


def main():
    palabra = input('Ingrese una palabra: ')
    palabra = separar_kword(palabra)
    palabra = sacar_mensaje(palabra)
    print(palabra)

if __name__ == '__main__':
    main()
