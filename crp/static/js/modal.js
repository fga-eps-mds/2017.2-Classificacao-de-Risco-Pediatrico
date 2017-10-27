$(document).ready(function() {
  $('form').on('hidden.bs.modal', function (e) {
    console.log("oi");
  //   $(this)
  //     .find("input,textarea,select")
  //        .val('')
  //        .end()
  //     .find("input[type=checkbox], input[type=radio]")
  //        .prop("checked", false)
  //        .end()
  //     .find("input[type=checkbox], input[type=radio]")
  //       .removeAttr('checked')
  //       .end();
  $(this).trigger('reset');
  })
} );
