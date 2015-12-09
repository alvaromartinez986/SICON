 $(document).ready(function () {
        $('#id_marca_carro').change(function () {
            var valor = $(this).val()
            if (valor=="")
            {
                valor=0
            }
            $.get("/dropdown_modelo",
                    {option: valor},
                    function (data) {
                        $('#id_modelo_carro').empty();
                        $('#id_modelo_carro').append("<option value=''>" + "-------" + "</option>");
                        if (data != "" ) {
                            var modelos = data.split(",");

                            for (var i = 0; i < modelos.length; i++) {
                                var modelo = (modelos[i]).split(":")
                                $('#id_modelo_carro').append("<option value='" + modelo[0] + "'>" + modelo[1] + "</option>");
                            }
                        }
                    });
        });
    });


