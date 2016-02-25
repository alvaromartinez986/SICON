/**
 * Created by fernando on 19/01/2016.
 */
$(document).ready(function() {
    var table = $('#vehiculos_venta').DataTable( {
        "scrollY": "200px",
        "paging": false
    } );

    table.column(4).visible( false );
    table.column(5).visible( false );
    table.column(6).visible( false );
    table.column(7).visible( false );


    $('a.toggle-vis').on( 'click', function (e) {
        e.preventDefault();

        // Get the column API object
        var column = table.column( $(this).attr('data-column') );

        // Toggle the visibility
        column.visible( ! column.visible() );
    } );
} );



