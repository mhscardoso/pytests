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

