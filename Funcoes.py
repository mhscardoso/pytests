# realiza os cálculos da função de 2° grau, retorna o valor de delta e suas raízes, se houver.

from math import sqrt

def eq_2_grau(a, b, c):
    x = 1
    y_x = (a * (x ** 2)) + (b * x) + c
    delta = (b ** 2) - 4 * a * c
    x_1 = ((-b) + sqrt(delta)) / (2 * a)
    x_2 = ((-b) - sqrt(delta)) / (2 * a)
    x_real = (-b) / (2 * a)
    if b < 0:
        print(f'y(x) = {a:.0f}x^2 {b:.0f}x + {c:.0f} = 0')
    else:
        print(f'y(x) = {a:.0f}x^2 - {b:.0f}x + {c:.0f} = 0')
    if delta == 0:
        print(f'DELTA = {b:.0f}^2 - 4*{a:.0f}*{c:.0f}')
        print(f'DELTA = {delta:.0f} (POSSUI 1 RAIZ)')
        print(f'RAIZ = {x_real}')
    elif delta < 0:
        print(f'DELTA = {b:.0f}^2 - 4*{a:.0f}*{c:.0f}')
        print(f'DELTA = {delta:.0f}')
        print('DELTA NEGATIVO, NÃO POSSUI RAIZ')
    elif delta > 0:
        print(f'DELTA = {b:.0f}^2 - 4*{a:.0f}*{c:.0f}')
        print(f'DELTA = {delta:.0f} (POSSUI 2 RAÍZES)')
        print(f'RAIZ 1 = {x_1:.0f}')
        print(f'RAIZ 2 = {x_2:.0f}')
    return y_x

a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))
eq_2_grau(a, b, c)



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
