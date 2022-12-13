import math 

def fibonacci(n):
    a = (1+math.sqrt(5))/2 
    b = (1-math.sqrt(5))/2 
    Edf = a**n + b**n
    return Edf

def main():
    n = int(input('Introduce un número: '))
    print(fibonacci(n))

if __name__ == '__main__':
    main()