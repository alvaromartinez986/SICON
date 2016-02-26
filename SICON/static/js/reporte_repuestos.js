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

function daysInMonth(month,year) {
    return new Date(year, month, 0).getDate();
}
