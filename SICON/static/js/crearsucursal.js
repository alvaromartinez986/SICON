
$(document).on('change','#id_departamento',function example(){
    $.ajax({
        url : "/sucursales/cargar_ciudades",
        type: "POST",
        data: $("#form_sucursal").serialize(),
        dataType: "json",

        success : function(data) {
            $('#id_ciudad').empty();
            var html_ciudades = "" ;
            for(var i = 0; i < data.length; i++) {
            html_ciudades = "<option value='" + data[i]["id"] +"'>" + data[i]["nombre"] + "</option>";
              $('#id_ciudad').append(html_ciudades);
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

