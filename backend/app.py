from flask import Flask, request, jsonify
from flask_cors import CORS
from chapter_1 import metodos
import sympy as sp

app = Flask(__name__)
CORS(app)

@app.route('/procesar', methods=['POST'])
def procesar_formulario():
    data = request.get_json()
    if data:
        print("Datos recibidos:")
        print(data)
        
        method = data.get("method")
        if method:
            function = data.get("function")
            a = data.get("a")
            b = data.get("b")
            tolerance = data.get("tolerance")
            n_iterations = data.get("nitter")
            x0 = data.get("initial_guess")
            a1= data.get("initial_guess1")
            b1 = data.get("initial_guess2")
            

            if method == "bisection":
                results = metodos.Bisection(function, a, b, tolerance, n_iterations)
                formatted_results = metodos.format_bisection_results(results)

            elif method == "false_position":
                results = metodos.Regla_falsa(function, a, b, tolerance, n_iterations)
                formatted_results = metodos.format_false_position_results(results)  

            elif method == "fixed_point":
                results = metodos.FixedPoint(function, x0, tolerance, n_iterations)
                formatted_results = metodos.format_fixed_point_results(results)

            elif method == "secant":
                results = metodos.Secant(function, a1, b1, tolerance, n_iterations)
                formatted_results = metodos.format_secant_results(results)

            elif method == "newton_raphson":
                results = metodos.NewtonRaphson(function, x0, tolerance, n_iterations)
                formatted_results = metodos.format_newton_raphson_results(results)

            elif method == "multiple_roots":
                results = metodos.MultipleRoots(function, x0, tolerance, n_iterations)
                formatted_results = metodos.format_multiple_roots_results(results)

            else:
                return "Método no válido"

            print(f"flask ({method}): ", formatted_results)
            return jsonify(formatted_results)  # Devuelve los resultados como JSON
        else:
            return "No se proporcionó un método en la solicitud."
    else:
        print("No se recibieron datos JSON en la solicitud.")
        return "No se recibió la información"


if __name__ == '__main__':
    app.run()
