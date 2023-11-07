function submitForm(event) {
    event.preventDefault();

    // Obtener los datos del formulario
    var formData = new FormData(event.target);

    // Crear un objeto que contenga los datos
    var data = {};
    formData.forEach(function(value, key) {
        // Convertir los valores a cadenas
        data[key] = value.toString();
    });

    // Realizar una solicitud fetch al servidor Flask
    fetch("http://localhost:5000/procesar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())  // Parsear la respuesta JSON del servidor
    .then(data => {
        // Actualizar el contenido de #result-container con la respuesta del servidor
        console.log(data)
        document.getElementById("false_positions_results").textContent = data.result;
    })
    .catch(error => console.error("Error:", error));
}
