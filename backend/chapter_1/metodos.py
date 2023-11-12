import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import threading


def funcion(func, x):
    return sp.sympify(func)

def Regla_falsa(ecua, a, b, tolerancia, x, max_iter):

    a = float(a)  # Convierte 'a' a número
    b = float(b)  # Convierte 'b' a número
    tolerancia = float(tolerancia)
    max_iter = int(max_iter)
    ecuacion = funcion(ecua, x)
    tramo = abs(b - a)
    fa = ecuacion.evalf(subs={x: a})
    fb = ecuacion.evalf(subs={x: b})
    resultados = []

    for iteracion in range(1, max_iter + 1):
        c = b - fb * (a - b) / (fa - fb)
        fc = ecuacion.evalf(subs={x: c})
        cambio = np.sign(fa) * np.sign(fc)
        resultado = {
            "Iteración": iteracion,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc,
            "Tramo": tramo
        }
        resultados.append(resultado)

        if cambio > 0:
            tramo = abs(c - a)
            a = c
            fa = fc
        else:
            tramo = abs(b - c)
            b = c
            fb = fc

        if tramo <= tolerancia:
            break

    return resultados, c, tramo

def plot_function(ecua, a, b, resultados, raiz, x):
    a = float(a)  # Convierte 'a' a número
    b = float(b)  # Convierte 'b' a número
    
    x_values = np.linspace(a, b, 400)
    y_values = [ecua.subs(x, xi) for xi in x_values]

    plt.plot(x_values, y_values, label=ecua, color='blue')
    plt.scatter(raiz, 0, color='red', marker='x', label='Root', zorder=5)

    # Anotar los resultados en el gráfico
    for resultado in resultados:
        plt.scatter(resultado["c"], 0, color='green', marker='o', label='c', zorder=5)

    plt.xlabel(x, fontweight='bold')
    plt.ylabel('f(x)', fontweight='bold')
    plt.legend()
    plt.grid()
    plt.show()

def main(fun, a, b, tol, max_iter):
    x = sp.symbols('x')
    ecuacion = funcion(fun, x)
    resultados, Raiz, Error = Regla_falsa(ecuacion, a, b, tol, x, max_iter)

    print("\nTabla de Resultados:")
    print("Iteración\t a\t\t b\t\t c\t\t f(c)\t\t Tramo")
    for resultado in resultados:
        print(f"{resultado['Iteración']}\t\t {resultado['a']:.6f}\t {resultado['b']:.6f}\t {resultado['c']:.6f}\t {resultado['f(c)']:.6f}\t {resultado['Tramo']:.6f}")

    print("\nRaiz:", Raiz)
    print("Error:", Error)

    # Graficar la función y los resultados
    plot_thread = threading.Thread(target=plot_function, args=(ecuacion, a, b, resultados, Raiz, x))
    plot_thread.start()
    #plot_thread.join()

    return resultados



