def pedir_numero():
    cadena = input('Introduce una cadena de caracteres: ')
    return cadena

def num_lista(numero):
    lista = [int(numeros) for numeros in numero]
    return lista

def lucky_ticket():
    numero2 = pedir_numero()
    numero = num_lista(numero2) 
    if len(numero) % 2 == 0:
        numero1 = numero[:int(len(numero)/2)]
        numero2 = numero[int(len(numero)/2):]
        suma1 = sum(numero1)
        suma2 = sum(numero2)
        if suma1 == suma2:
            return True
        else:
            return False
    else:
        numero1 = numero[:int((len(numero)+1)/2)]
        numero2 = numero[int((len(numero)-1)/2):]
        suma1 = sum(numero1)
        suma2 = sum(numero2)
        if suma1 == suma2:
            return True
        else:
            return False
        
def main():
    print(lucky_ticket())

if __name__ == '__main__':
    main()