# Novo código
# Lembrando que uma função de grau n sempre terá n raízes que poderão ser reais ou imaginárias. Portanto, uma função do segundo grau sempre possui 2(duas) raízes
# Aqui, o código mostra as raízes caso forem imaginárias, lembrando que j é a unidade imaginária. (j = sqrt(-1))

from math import sqrt
import cmath

def f2g(a, b, c):

    print(f'A função é da forma: {a:.0f}x2 + {b:.0f}x + {c:.0f}')
    
    d = (b**2) - (4 * a * c)

    try:
        root = sqrt(d)
    except:
        root = cmath.sqrt(d)
    
    x1 = (-b + root) / 2
    x2 = (-b - root) / 2

    if d > 0:
        print('A função possui duas raízes reais diferentes: ')
        print(f'x1 = {x1:.2f}')
        print(f'x2 = {x2:.2f}')    
    elif d == 0:
        print('A função possui duas raízes iguais: ')
        print(f'x1 = x2 = {x1:.2f}')
    
    else:
        print('A função possui duas raízes imaginárias:')
        print(f'x1 = {x1:.2f}')
        print(f'x2 = {x2:.2f}')
    
    return x1, x2


a = float(input('Coeficiente líder: '))
b = float(input('Coeficiente segundo: '))
c = float(input('Coeficiente independente: '))

f2g(a, b, c)



