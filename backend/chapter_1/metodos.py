import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import threading



def funcion(func, x):
    return sp.sympify(func)

def Regla_falsa(ecua, a, b, tolerancia, max_iter):
    x = sp.symbols('x')
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

def Bisection(ecua, a, b, tolerancia,max_iter):
    x = sp.symbols('x')
    a = float(a)
    b = float(b)
    tolerancia = float(tolerancia)
    max_iter = int(max_iter)
    ecuacion = funcion(ecua, x)
    fa = ecuacion.evalf(subs={x: a})
    fb = ecuacion.evalf(subs={x: b})
    resultados = []

    for iteracion in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = ecuacion.evalf(subs={x: c})
        cambio = np.sign(fa) * np.sign(fc)
        resultado = {
            "Iteración": iteracion,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc,
            "Tramo": abs(b - a)
        }
        resultados.append(resultado)

        if cambio > 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        if abs(b - a) < tolerancia:
            break

    return resultados, c, abs(b - a)

def FixedPoint(ecua, x0, tolerancia, max_iter):
    x = sp.symbols('x')
    x0 = float(x0)
    tolerancia = float(tolerancia)
    max_iter = int(max_iter)
    ecuacion = sp.sympify(ecua)
    resultados = []

    f = sp.lambdify(x, ecuacion, 'numpy')

    for iteracion in range(1, max_iter + 1):
        x1 = f(x0)
        x1 = max(-1e10, min(x1, 1e10))  # Limitar el valor absoluto de x
        resultado = {
            "Iteración": iteracion,
            "x": x1,  # Cambiado 'x1' a 'x'
            "g(x)": f(x1),  # Cambiado 'f(x1)' a 'g(x)'
            "Error": abs(x1 - x0)
        }
        resultados.append(resultado)

        if abs(x1 - x0) < tolerancia:
            break

        x0 = x1

    return resultados, x1, abs(x1 - x0)

def Secant(ecua, x0, x1, tolerancia, max_iter):
    x = sp.symbols('x')
    x0 = float(x0)
    x1 = float(x1)
    tolerancia = float(tolerancia)
    max_iter = int(max_iter)
    ecuacion = funcion(ecua, x)
    resultados = []

    for iteracion in range(1, max_iter + 1):
        f_x0 = ecuacion.evalf(subs={x: x0})
        f_x1 = ecuacion.evalf(subs={x: x1})
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        resultado = {
            "Iteración": iteracion,
            "x0": x0,
            "x1": x1,
            "x2": x2,
            "f(x2)": ecuacion.evalf(subs={x: x2}),
            "Error": abs(x2 - x1)
        }
        resultados.append(resultado)

        if abs(x2 - x1) < tolerancia:
            break

        x0 = x1
        x1 = x2

    return resultados, x2, abs(x2 - x1)

def NewtonRaphson(ecua, x0, tolerancia, max_iter):
    x = sp.symbols('x')
    x0 = float(x0)
    tolerancia = float(tolerancia)
    max_iter = int(max_iter)
    ecuacion = sp.sympify(ecua)
    derivada = sp.diff(ecuacion, x)
    f = sp.lambdify(x, ecuacion, 'numpy')
    f_prime = sp.lambdify(x, derivada, 'numpy')

    resultados = []

    for iteracion in range(1, max_iter + 1):
        # Verificar si la derivada es aproximadamente cero
        if abs(f_prime(x0)) < 1e-10:
            raise ValueError("La derivada se hizo cero. No se puede continuar con el método de Newton-Raphson.")

        x1 = x0 - f(x0) / f_prime(x0)

        resultado = {
            "Iteración": iteracion,
            "x0": x0,
            "x1": x1,
            "f(x1)": f(x1),
            "Error": abs(x1 - x0)
        }
        resultados.append(resultado)

        if abs(x1 - x0) < tolerancia:
            break

        x0 = x1

    return resultados, x1, abs(x1 - x0)

def MultipleRoots(ecua, x0, tolerancia, max_iter):
    x = sp.symbols('x')
    x0 = float(x0)
    tolerancia = float(tolerancia)
    max_iter = int(max_iter)
    ecuacion = funcion(ecua, x)
    derivada = sp.diff(ecuacion, x)
    resultados = []

    for iteracion in range(1, max_iter + 1):
        f_x0 = ecuacion.evalf(subs={x: x0})
        f_prime_x0 = derivada.evalf(subs={x: x0})
        x1 = x0 - f_x0 / f_prime_x0
        resultado = {
            "Iteración": iteracion,
            "x0": x0,
            "x1": x1,
            "f(x1)": ecuacion.evalf(subs={x: x1}),
            "Error": abs(x1 - x0)
        }
        resultados.append(resultado)

        if abs(x1 - x0) < tolerancia:
            break

        x0 = x1

    return resultados, x1, abs(x1 - x0)
       
def format_bisection_results(results):
    # Formatea los resultados específicos del método de bisección
    print("Results received in format_bisection_results:", results)

    resultados, raiz, error = results

    formatted_results = [
        {
            "Iteración": str(resultado["Iteración"]),
            "a": "{:.6f}".format(resultado['a']),
            "b": "{:.6f}".format(resultado['b']),
            "c": "{:.6f}".format(resultado['c']),
            "f(c)": "{:.6f}".format(resultado['f(c)']),
            "Tramo": "{:.6f}".format(resultado['Tramo'])
        }
        for resultado in resultados
    ]

    return formatted_results

def format_false_position_results(results):
    # Formatea los resultados específicos del método de posición falsa
    print("Results received in format_false_position_results:", results)

    resultados, c, tramo = results

    formatted_results = [
        {
            "Iteración": str(resultado["Iteración"]),
            "a": "{:.6f}".format(resultado['a']),
            "b": "{:.6f}".format(resultado['b']),
            "c": "{:.6f}".format(resultado['c']),
            "f(c)": "{:.6f}".format(resultado['f(c)']),
            "Tramo": "{:.6f}".format(resultado['Tramo'])
        }
        for resultado in resultados
    ]
    return formatted_results

def format_fixed_point_results(results):
    # Formatea los resultados específicos del método de punto fijo
    print("Results received in format_fixed_point_results:", results)

    resultados, raiz, error = results

    formatted_results = [
        {
            "Iteración": str(resultado["Iteración"]),
            "x": "{:.6f}".format(resultado['x']),  # Cambiado 'x1' a 'x'
            "g(x)": "{:.6f}".format(resultado['g(x)']),
            "Error": "{:.6f}".format(resultado['Error'])
        }
        for resultado in resultados
    ]

    return formatted_results

def format_secant_results(results):
    # Formatea los resultados específicos del método de la secante
    print("Results received in format_secant_results:", results)

    resultados, raiz, error = results

    formatted_results = [
        {
            "Iteración": str(resultado["Iteración"]),
            "x0": "{:.6f}".format(resultado['x0']),
            "x1": "{:.6f}".format(resultado['x1']),
            "x2": "{:.6f}".format(resultado['x2']),
            "f(x2)": "{:.6f}".format(resultado['f(x2)']),
            "Error": "{:.6f}".format(resultado['Error'])
        }
        for resultado in resultados
    ]

    return formatted_results


def format_newton_raphson_results(results):
    # Formatea los resultados específicos del método de Newton-Raphson
    print("Results received in format_newton_raphson_results:", results)

    resultados, raiz, error = results

    formatted_results = [
        {
            "Iteración": str(resultado["Iteración"]),
            "x0": "{:.6f}".format(resultado['x0']),
            "x1": "{:.6f}".format(resultado['x1']),
            "f(x1)": "{:.6f}".format(resultado['f(x1)']),
            "Error": "{:.6f}".format(resultado['Error'])
        }
        for resultado in resultados
    ]

    return formatted_results


def format_multiple_roots_results(results):
    # Formatea los resultados específicos del método de múltiples raíces
    print("Results received in format_multiple_roots_results:", results)

    resultados, raices, errores = results

    formatted_results = [
        {
            "Iteración": str(resultado["Iteración"]),
            "x0": "{:.6f}".format(resultado['x0']),
            "x1": "{:.6f}".format(resultado['x1']),
            "f(x1)": "{:.6f}".format(resultado['f(x1)']),
            "Error": "{:.6f}".format(resultado['Error'])
        }
        for resultado in resultados
    ]

    return formatted_results

