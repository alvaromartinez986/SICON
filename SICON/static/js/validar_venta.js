$('#form_venta_final').bootstrapValidator({
        message: 'Este valor no es valido',
        feedbackIcons:
        {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields:
        {
            codigos:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'El codigo del repuesto es requerido'
                    },

                }
            },
            descuentos:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'El porcentaje de descuento es requerido'
                    },
                    between: {
                            min: 0.0,
                            max: 100.0,
                            message: 'El descuento debe estar entre 0 y 100'
                        }
                }
            },
            precios:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'El precio del vehiculo es requerido'
                    },
                     digits:
                    {
                        message:'Debe introducir numeros'
                    }
                }
            },
            precios_finales:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'el precio final es requerido'
                    },
                    digits:
                    {
                        message:'debe introducir numeros'
                    }

                }

            }
        }
        });



