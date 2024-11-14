// const numeros = [1, 2, 3, 4];

// const somaTotal = numeros.reduce((acumulador, valorAtual) => {
//     return acumulador + valorAtual;
// }, 0);

// console.log(somaTotal);

const numeros = [1, 2, 3, 4];

const somaTotal = numeros.reduce((acumulador, valorAtual) => {
  return acumulador + valorAtual; // Operação definida no callback
}, 5); // O valor inicial do acumulador é 5

console.log(somaTotal); 

// acummulador 5
// 5+1+2+3+4
// 6+2+3+4
// 8+3+4
// 11+4
// 15


