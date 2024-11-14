// function somar (a, b, c){
//     let somatorio  = a + b + c;
//     return somatorio
// }

// console.log(somar(1,5,8))
// somar()



// ;function soma(a) {
//     return function(b) {
//         return function(c) {
//         return a + b + c;
//         };
//     };

// }soma()()()
// console.log(soma(1)(5)(8))
// // representa o mesmo cod so que no modelo currying
// modo mas fácil

function soma (num1){
    let acumulador = num1;
    return function soma2 (num2){
        if(!num2){
            return acumulador;
        }
        acumulador += num2;
        return soma2
    };
}
const resultado = soma(2)(4)(7)(3)();
console.log(resultado);
//modo mais complexo
