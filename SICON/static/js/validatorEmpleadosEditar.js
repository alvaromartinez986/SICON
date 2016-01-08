$('#form_empleado').bootstrapValidator({
        message: 'Este valor no es valido',
        feedbackIcons:
        {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields:
        {
            no_documento:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'Debe ingresar el número de documento'
                    },
                    digits:
                    {
                        message:'Debe introducir números'
                    }

                }

            },
            nombre:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'El nombre del empleado es requerido'
                    }
                }
            },
            apellido:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'El apellido del empleado es requerido'
                    }
                }
            },
            tipo_sangre:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'Debe seleccionar el tipo de sangre'
                    }

                }
            },
            experiencia:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'Debe ingresar el tiempo de experiencia'
                    },
                    digits:
                    {
                        message:'Debe introducir números'
                    }

                }

            },
            jornada:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'Debe seleccionar la jornada de trabajo'
                    }

                }
            },
            fecha_vinculacion:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'Debe ingresar la fecha de vinculación'
                    },
                    date: {
                        format: 'YYYY-MM-DD',
                        message: 'La fecha no es válida'
                    }

                }
            },
            telefono:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'Debe ingresar el teléfono de la sucursal'
                    },
                    digits:
                    {
                        message:'Debe introducir números'
                    }

                }

            },
            genero:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'Debe seleccionar el género del empleado'
                    }

                }
            },
            fecha_nacimiento:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'Debe ingresar la fecha de nacimiento'
                    },
                    date: {
                        format: 'YYYY-MM-DD',
                        message: 'La fecha no es válida'
                    }

                }
            },
            sucursal:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'Debe seleccionar la sucursal del empleado'
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
            username:
            {
                validators:
                {
                    notEmpty:
                    {
                        message: 'El nombre de usuario es requerido'
                    }
                }
            },
            password:
            {
                validators:
                {
                    identical:
                    {
                        field: 'password2',
                        message: 'Las contraseñas no coinciden'
                    }
                }
            },
            password2:
            {
                validators:
                {
                    identical:
                    {
                        field: 'password',
                        message: 'Las contraseñas no coinciden'
                    }
                }
            },
        }
        });



