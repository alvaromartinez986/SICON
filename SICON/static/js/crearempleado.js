
$(document).ready(function example(){
    $.ajax({
        url : "/sucursales/cargar_sucursales",
        type: "POST",
        data: $("#form_empleado").serialize(),
        dataType: "json",

        success : function(data) {
            $('#id_sucursal').empty();
            var html_sucursales = "" ;
            for(var i = 0; i < data.length; i++) {
            html_sucursales = "<option value='" + data[i]["id"] +"'>" + data[i]["nombre"] + "</option>";
              $('#id_sucursal').append(html_sucursales);
            }

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});

