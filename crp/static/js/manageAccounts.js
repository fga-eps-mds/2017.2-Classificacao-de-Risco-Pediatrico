$(document).ready(function() {
    $('#example').DataTable({
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
} );
