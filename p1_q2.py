import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial

### 2) Implemente uma função para realizar interpolação usando os nós de chebyshev. 
### A função deve receber o número de pontos desejados, o intervalo [a, b] e a função a ser interpolada.
### A função deve retornar o polinômio interpolador. 
### Em seguida, comparar graficamente a interpolação com nós de chebyshev e a interpolação com nós equidistantes para a função de Runge f(x) = 1/(x+25x^2) no intervalo [-1,1] usando 11 pontos.

def equidistant_nodes(n, a, b):
    return np.linspace(a, b, n)

def interpolate_poly(x_nodes, y_nodes):
    return np.polyfit(x_nodes, y_nodes, len(x_nodes) - 1)
    

def chebyshev_nodes(n, a, b, plot=False):
    k = np.arange(n)
    x = np.cos((2*k + 1) * np.pi / (2*n))
    nodes = 0.5 * (b - a) * x + 0.5 * (a + b)
    
    if plot:
        plt.figure(figsize=(10, 2))
        plt.scatter(nodes, np.zeros_like(nodes), c='red', marker='o')
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        plt.xlim(a-0.1, b+0.1)
        plt.title(f'Chebyshev Nodes (n={n}) in [{a}, {b}]')
        plt.grid(True)
        plt.show()
        plt.savefig('chebyshev_nodes.png', dpi=300)
        
    return nodes

def interpolate_chebyshev(n, a, b, func):
    x_cheb = chebyshev_nodes(n, a, b)
    y_cheb = func(x_cheb)
    poly_cheb = interpolate_poly(x_cheb, y_cheb)
    return poly_cheb, x_cheb, y_cheb

def runge_function(x):
    return 1 / (x + 25 * x**2)

def interpolate_equidistant(n, a, b, func):
    x_eq = equidistant_nodes(n, a, b)
    y_eq = func(x_eq)
    poly_eq = interpolate_poly(x_eq, y_eq)
    return poly_eq, x_eq, y_eq

def compare_interpolations(n, a, b, func):
    poly_cheb, x_cheb, y_cheb = interpolate_chebyshev(n, a, b, func)
    poly_eq, x_eq, y_eq = interpolate_equidistant(n, a, b, func)

    x_plot = np.linspace(a, b, 100)
    y_plot = func(x_plot)
    
    plt.figure(figsize=(12, 6))
    plt.plot(x_plot, y_plot, label='Runge Function', color='blue')
    plt.plot(x_plot, np.polyval(poly_cheb, x_plot), label='Chebyshev Interpolation', color='red')
    plt.plot(x_plot, np.polyval(poly_eq, x_plot), label='Equidistant Interpolation', color='green')
    
    plt.scatter(x_cheb, y_cheb, c='red', marker='o', label='Chebyshev Nodes')
    plt.scatter(x_eq, y_eq, c='green', marker='x', label='Equidistant Nodes')
    
    plt.title('Comparison of Chebyshev and Equidistant Interpolations')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.savefig('interpolation_comparison.png', dpi=300)
    plt.show()
    plt.savefig('interpolation_comparison.png', dpi=300)
    return poly_cheb, poly_eq

compare_interpolations(11, -1, 1, runge_function)