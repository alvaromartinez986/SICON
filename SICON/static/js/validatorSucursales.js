$('#form_sucursal').bootstrapValidator({
        message: 'Este valor no es valido',
        feedbackIcons:
        {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields:
        {
            nombre:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'el nombre de la sucursal es requerido'
                    }
                }
            },
            direccion:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'La dirección de la sucursal es requerida'
                    }
                }
            },
            telefono:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'debe ingresar el telefono de la sucursal'
                    },
                    digits:
                    {
                        message:'debe introducir numeros'
                    }

                }

            },

            ciudad:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'debe ingresar la Ciudad de la Sucursal'
                    }

                }
            }
        }
        });



