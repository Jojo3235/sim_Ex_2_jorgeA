import math 

def fibonacci(n):
    a = (1+math.sqrt(5))/2 
    b = (1-math.sqrt(5))/2 
    Edf = (1/math.sqrt(5))*a**n + (-1/math.sqrt(5))*b**n
    return Edf

def main():
    n = int(input('Introduce un número: '))
    print(fibonacci(n))

if __name__ == '__main__':
    main()