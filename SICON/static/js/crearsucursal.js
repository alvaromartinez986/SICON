
$(document).on('click','#id_departamento',function example(){
    $.ajax({
        url : "cargar_ciudades",
        type: "POST",
        data: $("#form_sucursal").serialize(),

        success : function(data) {
            $('#id_ciudad').empty();
            var ciudades = data.split(",");
            var html_ciudades;
            for(var i = 0; i < ciudades.length; i++) {
                var ciudad = (ciudades[i]).split(":")
                html_ciudades = "<option value='" + ciudad[0] + "'>" + ciudad[1] + "</option>";
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
