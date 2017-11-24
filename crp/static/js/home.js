$(document).ready(function () {

  $('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
  });


  $('.classification').on('click', function () {

    var $modal = $(this).closest('.modal');
    var $inputs = $modal.find(':input');

    var values = {};
    $inputs.each(function() {
      if (this.name === "patient_id" ||
          this.name === "form1" ||
          this.name === "form2" ||
          this.name === "form3" ||
          this.name === "form4" ||
          this.name === "form5" ) {
        values[this.name] = $(this).val();
      } else {
        values[this.name] = $(this).prop('checked');
      }
    });

    $.ajax({
      url: '/classify_patient/',
      dataType: 'json',
      data: values,
      success: function (data) {
        if (data) {
          $("#" + data["patient_id"] + " " + "#" + data["classification"]).prop('checked', true);
          $('#' + data["patient_id"]).modal('show');
          $('#classify-patient-' + data["patient_id"]).text("Depois de muita an na maniche learning chegamos a conclusão que o resultado é:"  +data["classification"]);
          $('#probability-' + data["patient_id"]).text(Math.max.apply(Math, data["probability"][0])*100 + "%");
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