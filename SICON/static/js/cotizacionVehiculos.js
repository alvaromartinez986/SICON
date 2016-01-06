/**
 * Created by family on 6/01/16.
 */

function getCheckboxes() {
    var table = document.getElementById("vehiculos_nuevos");
    var checkboxes = table.getElementsByTagName("input");
    var codCarros = [];
    var selected = 0;
    for (var i = 0; i < checkboxes.length; i++) {
        var checkbox = checkboxes[i];
        if(checkbox.checked){
            var currentRow = checkbox.parentNode.parentNode;
            var secondColumn = currentRow.getElementsByTagName("td")[1];
            selected++;
            codCarros[selected]=secondColumn.textContent;
        };
    }
    console.log(codCarros);
}
