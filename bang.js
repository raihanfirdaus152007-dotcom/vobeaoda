const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('masukan panjang = ', (inputPanjang) => {
  rl.question('masukan lebar = ', (inputLebar) => {
    
    let panjang = parseInt(inputPanjang);
    let lebar = parseInt(inputLebar);
    let luas = panjang * lebar;
    

    console.log('luas persegi panjang = ', luas);
    
    rl.close();
  });
});