# Novo código
# Lembrando que uma função de grau n sempre terá n raízes que poderão ser reais ou imaginárias. Portanto, uma função do segundo grau sempre possui 2(duas) raízes
# Aqui, o código mostra as raízes caso forem imaginárias, lembrando que j é a unidade imaginária. (j = sqrt(-1))


# A primeira para obter as raízes de números positivos - reais. A segunda, para obter a raíz de números negativos - imaginários.
from math import sqrt
import cmath

# A função recebe os valores a, b e c, que são os coeficientes da equação do segundo grau.
def f2g(a, b, c):
    
    # Verifica os valores inseridos na função.
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        k = -b/a

    # Aqui, verifica se o grau da função é, de fato 2, como deve ser.    
    except ZeroDivisionError:
        print('O coeficiente líder não pode ser nulo.')
        return None
    
    # Rejeita os erros de valores.
    except:
        print('Os valores digitados são inválidos.')
        return None
    
    else:
        # Mostra a forma da função.
        print(f'A função é da forma: {a:.0f}x2 + {b:.0f}x + {c:.0f}')

        # Calcula o delta da equação.
        d = (b**2) - (4 * a * c)

        # Tenta calcular a raíz de delta, se não for possível, d < 0 e, portanto, será necessário utilizar números complexos com a biblioteca cmath.
        try:
            root = sqrt(d)
        except:
            root = cmath.sqrt(d)

        # Calcula, enfim as raízes.        
        x1 = (-b + root) / (2 * a)
        x2 = (-b - root) / (2 * a)

        # Mostra para o usuário as três possíveis situações. Com d > 0 - duas raízes reais distintas - d = 0 - duas raízes iguais - e d < 0 - duas raízes imaginárias.
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

        # Retorna os valores das raízes.
        return x1, x2




