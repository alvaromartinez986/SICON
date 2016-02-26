/**
 * Created by fernando on 24/02/2016.
 */
function  ajax () {
    $('#fecha').change(function () {
        //extrayendo el rango de la consulta
        fecha = $("#fecha").val()
        gran = $("#btn").text().trim()
        console.log (gran)
        inicio = ""
        fin= ""
        if (gran == "Diario")
        {
            console.log("diario")
            inicio = fecha;
            fin= fecha;
        }
        else
        {
            if (gran == "Semanal")
            {
                console.log("semanal")
                split = fecha.split("/");
                inicio = split[0].trim();
                fin = split[1].trim();

            }
            else
            {
                console.log("mensual")
                inicio = fecha + "-01"
                split = fecha.split("-");
                num_days = daysInMonth(split[1],split[0])
                fin = fecha + "-"+ num_days;
            }
        }
        sucur = $("#btn-sucur").text().trim()
        $.get("repuestos_movimientos",
                {sucursal: sucur,inicio: inicio,fin: fin}, //datos enviados
            function (data) {
                console.log(data)
                cargar_tabla(data)
            })
        .fail(function() {
            alert ("ha ocurrido un error")
        })
    });
};

function daysInMonth(month,year) {
    return new Date(year, month, 0).getDate();
}

function cargar_tabla (data) {
    repuestos = JSON.parse(data);
    var table = $('<table data-graph-container="#grafico"data-graph-type="column"></table>').addClass('table table-bordered table-hover table-striped highchart');
    table.append('<thead> <tr> <th>Repuesto</th> <th>Entradas</th> <th>Salidas</th> </tr> </thead>')
    for (index in repuestos) {
        repuesto = repuestos[index]
        var row = $('<tr></tr>')
        row.append ($('<td></td>').text(repuesto.id))
        row.append ($('<td></td>').text(repuesto.entradas))
        row.append ($('<td></td>').text(repuesto.salidas))

        table.append(row);
    }

    $('#tabla').addClass('table-responsive');
    $('#tabla').empty();
    $('#tabla').append(table);
    $('table.highchart').highchartTable();
}
