var cleave = new Cleave('.date', {
    date: true,
    datePattern: ['d', 'm', 'Y']
});

var cleave = new Cleave('.cpf', {
    delimiters: ['.', '.', '-'],
    blocks: [3, 3, 3, 2],
    uppercase: true
});