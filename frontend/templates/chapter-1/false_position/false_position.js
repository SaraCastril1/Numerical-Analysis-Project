function submitForm(event) {
    event.preventDefault();

    // Obtener los datos del formulario
    var formData = new FormData(event.target);

    // Crear un objeto que contenga los datos
    var data = {};
    formData.forEach(function (value, key) {
        // Convertir los valores a cadenas
        data[key] = value.toString();
    });

    // Agregar el nombre del método al objeto data
    data["method"] = "false_position";
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
            // Crear y agregar la tabla con los resultados al elemento con el id "false_positions_results"
            var table = createTable(data);
            document.getElementById("false_positions_results").innerHTML = "";
            document.getElementById("false_positions_results").appendChild(table);
        })
        .catch(error => console.error("Error:", error));
}

// Función para crear la tabla
function createTable(data) {
    var table = document.createElement("table");
    table.classList.add("result-table"); // Puedes agregar una clase para darle estilo si es necesario

    // Crear encabezados de tabla
    var thead = document.createElement("thead");
    var headerRow = document.createElement("tr");
    for (var key in data[0]) {
        var th = document.createElement("th");
        th.textContent = key;
        headerRow.appendChild(th);
    }
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Crear cuerpo de tabla
    var tbody = document.createElement("tbody");
    data.forEach(function (item) {
        var row = document.createElement("tr");
        for (var key in item) {
            var cell = document.createElement("td");
            cell.textContent = item[key];
            row.appendChild(cell);
        }
        tbody.appendChild(row);
    });
    table.appendChild(tbody);

    return table;
}
