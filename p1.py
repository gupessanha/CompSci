### Questão 1 - Para a equação f(x) = x^3 - 3x^2 + 5x - 3 = 0:
### a) Escreva um programa que implemente o método de newton com uma estimativa inicial x_0 = 1.
### - Calcular e mostrar as 5 primeiras iterações ou menos, se convergir antes.
### - Para cada iteração, mostara: x_k, f(x_k), f'(x_k) e o erro relativo.
### - Utilizar tolerância de 10^-6 para convergência (critério de parada).

import numpy as np # type: ignore

func = lambda x: x**3 - 3*x**2 + 5*x - 3
derivada = lambda x: 3*x**2 - 6*x + 5

