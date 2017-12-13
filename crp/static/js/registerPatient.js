new Cleave('.date', {
  date: true,
  datePattern: ['d', 'm', 'Y']
});

new Cleave('.cpf', {
  delimiters: ['.', '.', '-'],
  blocks: [3, 3, 3, 2],
  uppercase: true
});

new Cleave('.cep', {
  delimiters: ['.', '-'],
  blocks: [2, 3, 3],
  uppercase: true
});

$('#id_birth_date').change(function () {
  var date_now = new Date();
  var convert_date = this.value.split('/');
  console.log(convert_date);
  var birth_date = new Date(convert_date[1] + '/' + convert_date[0] + '/' + convert_date[2]); // Or any other JS date
  var remainingDays = dateDiffInDays(birth_date, date_now);  //result = 1 mean the same day
  console.log(this.value);
  console.log(remainingDays);

  if (remainingDays >= 0 && remainingDays <= 28) {
    $('#id_age_range').val('1')
  }
  else if (remainingDays > 28 && remainingDays <= 90) {
    $('#id_age_range').val('2')
  }
  else if (remainingDays > 90 && remainingDays <= 730) {
    $('#id_age_range').val('3')
  }
  else if (remainingDays > 730 && remainingDays <= 3650) {
    $('#id_age_range').val('4')
  }
  else if (remainingDays > 3650) {
    $('#id_age_range').val('5')
  }
  else {
    $('#id_age_range').val('0')
  }

});

var _MS_PER_DAY = 1000 * 60 * 60 * 24;

// a and b are javascript Date objects
function dateDiffInDays(a, b) {
  // Discard the time and time-zone information.
  var utc1 = Date.UTC(a.getFullYear(), a.getMonth(), a.getDate());
  var utc2 = Date.UTC(b.getFullYear(), b.getMonth(), b.getDate());

  return Math.floor((utc2 - utc1) / _MS_PER_DAY);
}
