$(document).ready(function() {
  $('form').on('hidden.bs.modal', function (e) {
    console.log("oi");
  $(this).trigger('reset');
  })
} );
