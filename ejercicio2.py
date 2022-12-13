#crear diccionario con clave valor de los numeros del 1 al 9

numeros = {'uno': 1,
            'dos':2, 
            'tres':3, 
            'cuatro':4, 
            'cinco':5, 
            'seis':6, 
            'siete':7, 
            'ocho':8, 
            'nueve': 9}

def uno_num():
    return numeros['uno']

def dos_num():
    return numeros['dos']

def tres_num():
    return numeros['tres']

def cuatro_num():
    return numeros['cuatro']

def cinco_num():
    return numeros['cinco']

def seis_num():
    return numeros['seis']

def siete_num():
    return numeros['siete']

def ocho_num():
    return numeros['ocho']

def nueve_num():
    return numeros['nueve']

def main():
    print('Puedo escribir números como {},{},{}'.format(uno_num(),dos_num(),tres_num()))

if __name__ == '__main__':
    main()









