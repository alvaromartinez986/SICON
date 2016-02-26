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
                num_days = daysInMonth(fecha[1],fecha[0])
                fin = fecha + "-"+ num_days;
            }
        }
        sucur = $("#btn-sucur").text().trim()
        $.get("repuestos_movimientos",
            {sucursal: sucur,inicio: inicio,fin: fin}, //datos enviados
            function (data) {
                console.log(data)
            });
    });
};

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
    });



function daysInMonth(month,year) {
    return new Date(year, month, 0).getDate();
}
