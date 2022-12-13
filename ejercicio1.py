def separar_kword(palabra):
    palabra2 = palabra.split('#')
    return palabra2

def sacar_mensaje(palabra):
    for elemento in palabra:
        if elemento == '':
            palabra.remove(elemento)
            return palabra

def lista_a_string(palabra):
    palabra2 = ' '.join(palabra)
    return palabra2

def main():
    palabra = input('Ingrese una palabra: ')
    palabra = separar_kword(palabra)
    if '' in palabra[:1]:
        print('No se puede ingresar un # en medio del mensaje') 
    else:
        palabra = sacar_mensaje(palabra)
        palabra = lista_a_string(palabra)
        print(palabra)

if __name__ == '__main__':
    main()
