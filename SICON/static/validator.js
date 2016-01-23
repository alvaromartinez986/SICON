$('#form_repuesto').bootstrapValidator({
        message: 'Este valor no es valido',
        feedbackIcons:
        {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields:
        {
            codigo:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'El codigo del repuesto es requerido'
                    }
                }
            },
            nombre:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'el nombre del repuesto es requerid'
                    }
                }
            },
            marca:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'La marca del repuesto es requerida'
                    }
                }
            },
            costo:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'debe ingresar el costo del repuesto'
                    },
                      between: {
                            min: 0,
                            max: 2147483647,
                            message: 'El costo debe ser menor a 2.147\'483.647'
                        }

                    }
                },

            cantidad:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'debe ingresar la cantidad'
                    },
                    between: {
                            min: 0,
                            max: 2147483647,
                            message: 'El cantidad debe ser menor a 2.147\'483.647'
                        }

                }
            }
        }
        });



