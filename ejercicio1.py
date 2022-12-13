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

def index_no_nulos_lista(lista):
    for elemento in lista:
        if elemento != '':
            return lista.index(elemento)

def main():
    palabra = input('Ingrese una palabra: ')
    if palabra[0] == '#':
        palabra = separar_kword(palabra)
        index = index_no_nulos_lista(palabra)
        if len(palabra[index:])>1:
            print(list())
        else:
            palabra = sacar_mensaje(palabra)
            palabra1 = lista_a_string(palabra)
            if palabra1[0].isalpha() == True:
                print(palabra1)
            else:
                print('No se pueden escribir caracteres especiales o numericos al inicio del mensaje')
    else:
        print('El mensaje ha de empezar por #')

if __name__ == '__main__':
    main()