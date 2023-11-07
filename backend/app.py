from flask import Flask, request
from flask_cors import CORS
from chapter_1 import metodos
from flask import jsonify

app = Flask(__name__)
CORS(app) 

@app.route('/procesar', methods=['POST'])
def procesar_formulario():
    data = request.get_json()
    if data:
        print("Datos recibidos:")
        print(data)
        results = metodos.main(data.get("function"), data.get("a"), data.get("b"), data.get("tolerance"), data.get("nitter"))
        # Convertir los valores de punto flotante a cadenas
        results = [
            {
                "Iteración": str(result["Iteración"]),
                "a": str(result["a"]),
                "b": str(result["b"]),
                "c": str(result["c"]),
                "f(c)": str(result["f(c)"]),
                "Tramo": str(result["Tramo"])
            }
            for result in results
        ]
        print("flask: ", results)
        return jsonify(results)  # Devuelve los resultados como JSON
    else:
        print("No se recibieron datos JSON en la solicitud.")
        return "no se recibió la información"


if __name__ == '__main__':
    app.run()

