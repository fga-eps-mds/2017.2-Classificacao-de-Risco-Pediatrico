// var cleave = new Cleave('.date', {
//     date: true,
//     datePattern: ['d', 'm', 'Y']
// });

var cleave = new Cleave('.cpf', {
    delimiters: ['.', '.', '-'],
    blocks: [3, 3, 3, 2],
    uppercase: true
});

$('#id_birth_date').change(function(){
  var date_now    = new Date();
  var convert_date = this.value.split('/')
  console.log(convert_date)
  var birth_date    = new Date(convert_date[1]+'/'+convert_date[0]+'/'+convert_date[2]); // Or any other JS date
  var remainingDays    = dateDiffInDays(birth_date, date_now);  //result = 1 mean the same day
  console.log(this.value)
  console.log(remainingDays)
  // console.log(date_now)
  if (remainingDays >= 0 && remainingDays <= 28){
    $('#age_range').val('1')
  }
  else if (remainingDays > 28 && remainingDays <= 90){
    $('#age_range').val('2')
  }
  else if (remainingDays > 90 && remainingDays <= 730){
    $('#age_range').val('3')
  }
  else if (remainingDays > 730 && remainingDays <= 3650){
    $('#age_range').val('4')
  }
  else if (remainingDays > 3650){
    $('#age_range').val('5')
  }
  else{
    $('#age_range').val('0')
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
