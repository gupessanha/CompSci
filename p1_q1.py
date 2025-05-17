### Questão 1 - Para a equação f(x) = x^3 - 3x^2 + 5x - 3 = 0:
### a) Escreva um programa que implemente o método de newton com uma estimativa inicial x_0 = 1.
### - Calcular e mostrar as 5 primeiras iterações ou menos, se convergir antes.
### - Para cada iteração, mostara: x_k, f(x_k), f'(x_k) e o erro relativo.
### - Utilizar tolerância de 10^-6 para convergência (critério de parada).

import numpy as np # type: ignore

pattern = [
    "   A    ",
    "  A A   ",
    " A   A  ",
    "A     A ",
    "AAAAAAA ",
    "A     A ",
    "A     A ",
    "A     A "
]

for line in pattern:
    print(line)
print()

def newton_a(func, derivada, x_0, tol=1e-6, max_iter=5):
    """
    Aglrotimo do método de Newton
    1. Escolher uma aproximação inicial para x_0
    2. Calcular x_1 = x_0 - f(x_0)/f'(x_0)
    3. Verificar o erro |x_k - x_k_-1| / |x_k| < tol
    4. Se o erro for menor que a tolerância aceitar x1 como solução;
        caso contrário, atualizar x_0 = x_1 e repetir o passo 2.

    Args: 
        func (function): função a ser resolvida
        derivada (function): derivada da função
        x_0 (float): valor inicial
        tol (float): tolerância para convergência
        max_iter (int): número máximo de iterações
    """

    x_k = x_0
    for i in range(max_iter):
        f_xk = func(x_k)
        f_prime_xk = derivada(x_k)
        if i == 0:
            erro_relativo = float('nan')
        else:
            erro_relativo = abs(x_k - x_k_1) / abs(x_k)
        print(f"Iteração {i+1}: x_k = {x_k:.6f}, f(x_k) = {f_xk:.6f}, f'(x_k) = {f_prime_xk:.6f}, erro relativo = {erro_relativo:.6e}")

        if i != 0 and erro_relativo < tol:
            print("Convergência alcançada.")
            return x_k

        x_k_1 = x_k
        x_k = x_k - f_xk / f_prime_xk

    print("Número máximo de iterações atingido.")
    return x_k

# Testando o código para a equação f(x) = x^3 - 3x^2 + 5x - 3
print("+=+=+"*20)
print("x**3 - 3*x**2 + 5*x - 3")
func = lambda x: x**3 - 3*x**2 + 5*x - 3
derivada = lambda x: 3*x**2 - 6*x + 5
newton_a(func, derivada, 1)

### Testando código para outras equações 
print ("+=+=+"*20)
print("x**2 - 2")
func = lambda x: x**2 - 2
derivada = lambda x: 2*x
newton_a(func, derivada, 1)

print("+=+=+"*20)
print("x**3 - 5")
func = lambda x: x**3 - 5
derivada = lambda x: 3*x**2
newton_a(func, derivada, 1)

print("+=+=+"*20)

### b) Modifique o programa para detectar possíveis falhas do método:
### - Se a derivada for zero está próxima de 0 ou é igual a 0
### - Se |x_k| excede um limite razoável (divergência)
### - Determinar se o método está oscilando sem convergir

def newton_b(func, derivada, x_0, tol=1e-6, max_iter=5):
    """
    Aglrotimo do método de Newton
    1. Escolher uma aproximação inicial para x_0
    2. Calcular x_1 = x_0 - f(x_0)/f'(x_0)
    3. Verificar o erro |x_k - x_k_-1| / |x_k| < tol
    4. Se o erro for menor que a tolerância aceitar x1 como solução;
        caso contrário, atualizar x_0 = x_1 e repetir o passo 2.

    Args: 
        func (function): função a ser resolvida
        derivada (function): derivada da função
        x_0 (float): valor inicial
        tol (float): tolerância para convergência
        max_iter (int): número máximo de iterações
    """

    x_k = x_0
    for i in range(max_iter):
        f_xk = func(x_k)
        f_prime_xk = derivada(x_k)
        if i == 0:
            erro_relativo = float('nan')
        else:
            erro_relativo = abs(x_k - x_k_1) / abs(x_k)
        print(f"Iteração {i+1}: x_k = {x_k:.6f}, f(x_k) = {f_xk:.6f}, f'(x_k) = {f_prime_xk:.6f}, erro relativo = {erro_relativo:.6e}")

        if abs(f_prime_xk) < tol:
            print("Derivada próxima de zero. Método pode falhar.")
            return None

        if abs(x_k) > 1e10:
            print("Solução divergiu.")
            return None

        if i != 0 and abs(erro_relativo) < tol:
            print("Convergência alcançada.")
            return x_k

        if i != 0 and abs(x_k - x_k_1) < tol:
            print("Método oscilando sem convergir.")
            return None

        x_k_1 = x_k
        x_k = x_k - f_xk / f_prime_xk

    print("Número máximo de iterações atingido.")
    return x_k

# Desenho do padrão "Letra B"

pattern = [
    "BBBBBBB ",
    "B      B",
    "B      B",
    "BBBBBBB ",
    "BBBBBBB ",
    "B      B",
    "B      B",
    "BBBBBBB "
]

for line in pattern:
    print(line)
print()

# Testando o código para a equação f(x) = x^3 - 3x^2 + 5x - 3
print("+=+=+"*20)
print("x**3 - 3*x**2 + 5*x - 3")
func = lambda x: x**3 - 3*x**2 + 5*x - 3
derivada = lambda x: 3*x**2 - 6*x + 5
newton_a(func, derivada, 1)

print ("+=+=+"*20)
print("x**2 - 2")
func = lambda x: x**2 - 2
derivada = lambda x: 2*x
newton_b(func, derivada, 1)
print("+=+=+"*20)

print("x**3 - 5")
func = lambda x: x**3 - 5
derivada = lambda x: 3*x**2
newton_b(func, derivada, 1)
print("+=+=+"*20)

### c) Investique o comportamento do método para diferentes pontos iniciais: x_0 = 0, x_0 = 2, x_0 = 3.
### Discuta seus resultados, explicando comporamentos inesperados.

pattern = [
    " CCCCC  ",
    "C     C ",
    "C       ",
    "C       ",
    "C       ",
    "C       ",
    "C     C ",
    " CCCCC  "
]

for line in pattern:
    print(line)
print()

for x_o in [0, 1, 2, 3]:    
    print("+=+=+"*20)
    print("x**3 - 3*x**2 + 5*x - 3,", f"x_o = ", x_o)
    func = lambda x: x**3 - 3*x**2 + 5*x - 3
    derivada = lambda x: 3*x**2 - 6*x + 5
    newton_b(func, derivada, x_o)

"""
A função tem uma raiz real em x=1.
O método converge rapidamente se o chute inicial estiver próximo da raiz.
O número máximo de iterações fixo em 5 limita a convergência completa em alguns casos.
Mesmo com valores grandes de entrada, o método mostra robustez.
A curvatura da função influencia muito: quanto mais suave a derivada, melhor o desempenho.
O teste de abs(x_k - x_k_1) < tol como critério para "método oscilando sem convergir" é redundante com o erro relativo e pode ser removido ou ajustado para evitar falso positivo.

1. Função e derivada:
   - f(x) = x³ - 3x² + 5x - 3
   - f'(x) = 3x² - 6x + 5
   - Tolerância: 1e-6
   - Máximo de iterações: 5

2. Caso x₀ = 0:
   - f(0) = -3, f'(0) = 5
   - A solução se aproxima de x ≈ 1.0
   - Erro vai diminuindo a cada iteração
   - Convergência clara, mas limitada pelo número de iterações

3. Caso x₀ = 1:
   - f(1) = 0, f'(1) = 2
   - A raiz já é encontrada na primeira iteração
   - Convergência imediata
   - Método finaliza rapidamente e com sucesso

4. Caso x₀ = 2:
   - f(2) = 3, f'(2) = 5
   - Método converge em direção a x ≈ 1.0
   - Evolução semelhante ao caso x₀ = 0
   - Boa aproximação, mas a tolerância não é atingida em 5 iterações

5. Caso x₀ = 3:
   - f(3) = 12, f'(3) = 14
   - Método apresenta oscilações, mas caminha para a raiz
   - Último valor fica próximo de x ≈ 1.0008
   - Erro relativo ainda significativo na última iteração
   """