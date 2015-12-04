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
                    digits:
                    {
                        message:'debe introducir numeros'
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
                    digits:
                    {
                        message:'debe introducir numeros'
                    }

                }
            }
        }
        });



