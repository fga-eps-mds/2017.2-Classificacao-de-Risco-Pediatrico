$(document).ready(function() {
      var table = $('#example').DataTable( {
        order: [[1,'desc']],
        responsive: true,
        "lengthMenu": [ 50, 75, 100 ],
        "columnDefs": [
            {
                "orderable": false,
                "targets": [ 0,1,2,3,4 ]
            }
        ],
        "language": {
            "lengthMenu": "Mostrar _MENU_ por página",
            "zeroRecords": "Nenhum paciente encontrado",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            "infoEmpty": "Nenhuma informação disponível",
            "infoFiltered": "(Filtrado de _MAX_ registros)",
            "search": "Procurar:",
            "paginate": {
                "previous": "Anterior",
                "next": "Próximo"
            }
        }
    } );

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

    $('#example_filter').hide();

    $('#searchPatient').on( 'keyup', function () {
        table.search( this.value ).draw();
    });

});

function changeGradientWidth(element) {
    var containerBox = element.parentNode.parentNode;

    if(containerBox.style.paddingRight === "7px")
        containerBox.style.paddingRight = "0px";
    else {
        containerBox.style.paddingRight = "7px";
    }
}
