let num = [1,2,3,34,23,76,4,5,20]
num.sort((a,b) => a - b)
console.log(num)


// const frutas = ['banana maça', 'banana prata', 'acerola', 'uva', 'goiaba']
// const resultado = frutas.filter ((tipo) => tipo.includes('banana'))
// console.log(resultado)


const numeros = [1,2,3,4,5,6,7,23,24,25,26,27,28]
const numerosPares = numeros.filter((numero) => numero % 2 === 0)
console.log(numerosPares) 