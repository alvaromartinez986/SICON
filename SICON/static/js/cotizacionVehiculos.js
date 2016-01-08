/**
 * Created by family on 6/01/16.
 */

function getCheckboxes() {
    var table = document.getElementById("vehiculos_nuevos");
    var checkboxes = table.getElementsByTagName("input");
    var carros = [];
    var selected = 0;
    for (var i = 0; i < checkboxes.length; i++) {
        var checkbox = checkboxes[i];
        if(checkbox.checked){
            var currentRow = checkbox.parentNode.parentNode;
            var row = currentRow.getElementsByTagName("td");
            selected++;
            carros[selected]=row;
        }
    }
    return carros;
}

function writeCotizacion(){
    var carros = getCheckboxes();
    var identificacion  = $('body').data('identificacion');
    var ruta = "cotización"+ identificacion+".pdf";
    var tabla = [];
    var firstRow = [{ text: 'Cilindraje', bold: true }, { text: 'Marca', bold: true }, { text: 'Linea', bold: true }, { text: 'Modelo', bold: true }, { text: 'Tipo de Combustible', bold: true },{ text: 'Color', bold: true },{ text: 'Valor', bold: true }];
    tabla.push(firstRow);
    for (var i=0;i<carros.length;i++){
        carros.length
        var newRow=[];
        console.log(carros);
        for(var j=0;j<carros[i].length;j++){
            if(j!==0&&j!==1) {
                newRow.push(carros[i][j].textContent);
            }
        }
        tabla.push(newRow);
    }
    var docDefinition = {
      content: [
        'Esta es la cotizacion hecha al cliente '+identificacion+':',

        {
          table: {
            // headers are automatically repeated if the table spans over multiple pages
            // you can declare how many rows should be treated as headers
            headerRows: 1,
            widths: [ '*', 'auto', 100, '*' ],

            body: tabla
          }
        }
      ]
    };
    pdfMake.createPdf(docDefinition).download(ruta);

}