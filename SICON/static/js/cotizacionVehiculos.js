/**
 * Created by family on 6/01/16.
 */

function getCheckboxes() {
    var table = document.getElementById("vehiculos_nuevos");
    var checkboxes = table.getElementsByTagName("input");
    var carros = [];
    var valorTotal=0;
    for (var i = 0; i < checkboxes.length; i++) {
        var checkbox = checkboxes[i];
        if(checkbox.checked){
            var currentRow = checkbox.parentNode.parentNode;
            var row = currentRow.getElementsByTagName("td");
            valorTotal+=parseInt(row[8].textContent);
            var arrayRow = [row[2].textContent,row[3].textContent, row[4].textContent,row[5].textContent,row[6].textContent,row[7].textContent,row[8].textContent]
            console.log(arrayRow);
            carros.push(arrayRow);
        }
    }
    carros.push(valorTotal);
    return carros;
}

function writeCotizacion(){
    var carros = getCheckboxes();
    var valorTotal = carros[carros.length-1];
    carros.length=carros.length-1;
     var d = new Date();
    var meses = new Array ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre");
    var fecha = d.getDate() + " de " + meses [(d.getMonth() +1)] + " del " + d.getFullYear();
    var identificacion  = $('body').data('identificacion');
    var nombres = $('body').data('nombres');
    var apellidos = $('body').data('apellidos');
    var ruta = "cotización"+ identificacion+".pdf";
    var firstRow = [{ text: 'Cilindraje', bold: true }, { text: 'Marca', bold: true }, { text: 'Linea', bold: true }, { text: 'Modelo', bold: true }, { text: 'Tipo de Combustible', bold: true },{ text: 'Color', bold: true },{ text: 'Valor (COP)', bold: true }];
    var tabla= [firstRow];
    for (carro in carros){
        tabla.push(carros[carro]);
    }
    console.log(tabla);
    var docDefinition = {
      content: [
          { text: 'COTIZACIÓN SICON', style: 'header' },
        { text: 'Fecha : ' + fecha + '\n \n', bold:true, alignment: 'right',fontSize : 18  },
        {
          stack: [
            // second column consists of paragraphs
            { text: 'CLIENTE', bold: true },
            'Identificacion : ' + identificacion,
            'Nombres : ' + nombres,
            'Apellidos : ' + apellidos,
          ],
          fontSize: 15
        },
          { text: '\n \n' },

        {
          table: {
            body:tabla

          }
        },
          {text:'El valor total de la cotización es: '+valorTotal+' COP', bold:true, alignment: 'right' }
      ]
    };
    pdfMake.createPdf(docDefinition).download(ruta);

}