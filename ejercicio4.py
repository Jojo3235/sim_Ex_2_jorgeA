def pedir_numero():
    cadena = input('Introduce una cadena de caracteres: ')
    return cadena

def lucky_ticket():
    numero = pedir_numero()
    if len(numero) % 2 == 0:
        numero1 = numero[:len(numero)//2]
        numero2 = numero[len(numero)//2:]
        suma1 = sum(numero1)
        suma2 = sum(numero2)
        if suma1 == suma2:
            return True
        else:
            return False
    else:
        numero1 = numero[:(len(numero)+1)//2]
        numero2 = numero[(len(numero)-1)//2:]
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