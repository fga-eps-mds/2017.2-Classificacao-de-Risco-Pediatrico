$(document).ready(function() {
    var table = $('#example').DataTable({
        "language": {
            "lengthMenu": "Mostrar _MENU_ por página",
            "zeroRecords": "Nada encontrado - Desculpe :(",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            "infoEmpty": "",
            "infoFiltered": "(Filtrado de _MAX_ registros)",
            "search": "Procurar:",
            "paginate": {
                "previous": "Anterior",
                "next": "Próximo"
            }
        }
    });
    $('#example_filter').hide()
    //$('#example_length').hide()
    // $('#example_info').hide()
    // $('#example_paginate').hide()
    $('#searchPatient').on( 'keyup', function () {
        table.search( this.value ).draw();
    } );
} );
