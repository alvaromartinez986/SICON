/**
 * Created by fernando on 24/02/2016.
 */
function  ajax () {
    $('#fecha').change(function () {
        $("#id_linea").val($( "#id_linea option:selected" ).text()).trigger("change");
    });
}

    $('#btn-sucur').click(function () {
        $("#id_linea").val($( "#id_linea option:selected" ).text()).trigger("change");
    });

    $('#id_marcas').change(function () {

        lin = $( "#id_marcas option:selected" ).text();
        $.get("devuelve_lineas",
            {linea: lin}, //datos enviados
            function (data) {
                $('#id_linea').empty();
                var html_lineas = "" ;
                html_linea1 = "<option>Todas</option>";
                $('#id_linea').append(html_linea1);
                for(var i = 0; i < data.length; i++) {
                html_lineas = "<option>" + data[i]["nombre"] + "</option>";
                  $('#id_linea').append(html_lineas);
                }
            });
        $("#id_linea").val("Todas").trigger("change");
    });

    $('#id_linea').change(function () {
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



        mar = $( "#id_marcas option:selected" ).text();
        lin = $( "#id_linea option:selected" ).text();
        sucur = $("#btn-sucur").text().trim();
        $.get("modelos_vendidos",
            {linea: lin, marca: mar, sucursal: sucur, inicio:inicio, fin:fin}, //datos enviados
            function (data) {
                repuestos = data;
                var table = $('<table data-graph-container="#grafico"data-graph-type="column"></table>').addClass('table table-bordered table-hover table-striped highchart');
                table.append('<thead> <tr> <th>Nombre</th> <th>Total</th> </tr> </thead>')
                for (index in repuestos) {
                    repuesto = repuestos[index]
                    var row = $('<tr></tr>')
                    row.append ($('<td></td>').text(repuesto.nombre))
                    row.append ($('<td></td>').text(repuesto.valor))

                    table.append(row);
    }

    $('#tabla').addClass('table-responsive');
    $('#tabla').empty();
    $('#tabla').append(table);
    $('table.highchart').highchartTable();

            });
    });

function daysInMonth(month,year) {
    return new Date(year, month, 0).getDate();
}
