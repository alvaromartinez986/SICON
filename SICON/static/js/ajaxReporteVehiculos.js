/**
 * Created by nelson on 25/02/16.
 */
function  ajaxReporteVehiculos () {
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
                console.log("SEMANAL DATA",inicio,fin);
            }
            else
            {
                console.log("mensual")
                inicio = fecha + "-01"
                split = fecha.split("-");
                num_days = daysInMonth(split[1],split[0])
                //console.log("NUMERO DIAS:",split[1],split[0])
                fin = fecha + "-"+ num_days;
                console.log("MENSUAL DATA",inicio,fin);
            }
        }
        sucur = $("#btn-sucur").text().trim()
        $.get("data_vehiculos",
            {sucursal: sucur,inicio: inicio,fin: fin}, //datos enviados
            function (data) {
                datos=JSON.parse(data);

                var listamodelos=[];
                var x=0
                var table = $('<table id=tablareportevehiculos2></table>').addClass('table table-striped table-bordered table-hover');
                table.append ('<thead> <tr><th>Código</th><th>Cilindraje</th><th>Línea</th><th>Modelo</th><th>Tipo de combustible</th><th>Color</th><th>Marca</th><th>Valor</th><th>Fecha</th></tr> </thead>')
                for (carro in datos){
                    vehiculoss = datos[carro];
                    //console.log("MARCA EN JSON:",vehiculoss.marca)
                    var row = $('<tr></tr>')
                    var column = $('<td></td>').text(vehiculoss.id)
                    row.append(column)
                    var column = $('<td></td>').text(vehiculoss.cilindraje)
                    row.append(column)
                    var column = $('<td></td>').text(vehiculoss.linea)
                    row.append(column)
                    var column = $('<td></td>').text(vehiculoss.modelo);

                    row.append(column)
                    var column = $('<td></td>').text(vehiculoss.tipo_combustible)
                    row.append(column)
                    var column = $('<td></td>').text(vehiculoss.colors)
                    row.append(column)
                    var column = $('<td></td>').text(vehiculoss.marca);
                    listamodelos[x]=vehiculoss.marca;
                    row.append(column)
                    var column = $('<td></td>').text(vehiculoss.valor)
                    row.append(column)
                    var column = $('<td></td>').text(vehiculoss.fecha)
                    row.append(column)
                    table.append(row);
                    x=x+1;
                }

    //            Funcion Contador:
                var mayor=0;
                var contador=0;
                //console.log(listamodelos);

                var k = {};

                //push into hashtable
                for(i in listamodelos){
                 k[listamodelos[i]]=(k[listamodelos[i]]||0)+1; //increments count if element already exists
                }

                var valoresmarcas=[]
                var y=0
                //result
                for(var j in k) {
                    //console.log(j+" comes -> "+k[j]+" times");
                    valoresmarcas[y]=k[j]
                    y=y+1
                }
                mayor=Math.max(... valoresmarcas);
                console.log("Mayor:",mayor);

                var MarcaMayor
                for(var q in k) {
                    if(k[q]==mayor){
                        MarcaMayor=q
                    }
                    }
                console.log(MarcaMayor);


        document.getElementById('labelNombreModelo').innerHTML ="modelo "+MarcaMayor+" Con ";
                document.getElementById('labelNumero').innerHTML =mayor;




    $('#tablas').addClass('table-responsive');
    $('#tablas').empty();
    $('#tablas').append(table);



                $(document).ready(function() {
    // Setup - add a text input to each footer cell
          var i=0;
          $('#tablareportevehiculos2 tfoot th').each( function () {
              i++;
              if (i <=10){
              var title = $(this).text();
              $(this).html( '<input type="text" placeholder='+title+' style="width: 100%;" />' );}
          } );

        // DataTable
            var table = $('#tablareportevehiculos2').DataTable({responsive:true});

            // Apply the search
            table.columns().every( function () {


                var that = this;

            $( 'linea', this.footer() ).on( 'keyup change', function () {
                if ( that.search() !== this.value ) {
                    that
                        .search( this.value )
                        .draw();
                }
        } );
    } );
} );


            });


    });



}



function daysInMonth(month,year) {
    return new Date(year, month, 0).getDate();
}