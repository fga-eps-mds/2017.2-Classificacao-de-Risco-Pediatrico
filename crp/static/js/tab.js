console.log('tab');
$('#crp-tab li:nth-of-type(1)').click(function (e) {
  $('.tab-content input').val('admin');
  console.log('1');
});

$('#crp-tab li:nth-of-type(2)').click(function (e) {
  $('.tab-content input').val('atendente');
  console.log('2');
});

$('#crp-tab li:nth-of-type(3)').click(function (e) {
  $('.tab-content input').val('recepcionista');
  console.log('3');
});