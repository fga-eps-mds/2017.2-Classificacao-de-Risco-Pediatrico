$(document).ready(function () {
  $('#example').DataTable({
    "responsive": true,
    "order": [[2, 'desc']],
    "columnDefs": [{
      "targets": "_all",
      "orderable": false
    }],
    "lengthMenu": [50, 75, 100],
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
  });

  table = $('#example').DataTable()
  $('#searchPatient').keyup(function(){
    table.column(1).search($(this).val()).draw() ;
  })

  $('#example_filter').hide();

  $('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
  });

  $('.classification').on('click', function () {

    var $modal = $(this).closest('.modal');
    var $inputs = $modal.find(':input');

    var values = {};
    $inputs.each(function () {
      if (this.name === "patient_id" ||
        this.name === "form1" ||
        this.name === "form2" ||
        this.name === "form3" ||
        this.name === "form4" ||
        this.name === "form5") {
        values[this.name] = $(this).val();
      } else {
        values[this.name] = $(this).prop('checked');
      }
    });

    $.ajax({
      url: '/classify_patient/',
      type: 'POST',
      dataType: 'json',
      data: values,
      success: function (data) {
        if (data) {
          $("#" + data["patient_id"] + " " + "#" + data["classification"]).prop('checked', true);
          $('#' + data["patient_id"]).modal('show');
          $('#classify-patient-' + data["patient_id"]).text("Recomendado encaminhar para "
            + data["classification"]);
          $('#probability-' + data["patient_id"]).text("Porcentagem de Confiabilidade: "
            + (Math.max.apply(Math, data["probability"][0]) * 100).toFixed(1) + "%");
        }
      }
    });
  });
});

function changeGradientWidth(element) {
  var containerBox = element.parentNode.parentNode;

  if (containerBox.style.paddingRight === "7px")
    containerBox.style.paddingRight = "0px";
  else {
    containerBox.style.paddingRight = "7px";
  }
}
