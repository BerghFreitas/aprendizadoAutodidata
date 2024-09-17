/*function criaContador (){
    let contador = 0;
    
    return function (){
        contador += 1;
        return contador; //closure e o conseito de que a funcao interna consegoe acessar a variavel externa mesmo depois ter finalizada
    };
    
}
const meuContador = criaContador();
console.log(meuContador());
console.log(meuContador());
console.log(meuContador());
console.log(meuContador());

*/

function criarSaudacao (nome){
    return function(){
        console.log(`ola ${nome}`);
    };
}
const saudacaojoao = criarSaudacao('joao');
const saudacaoMaria = criarSaudacao('maria');

saudacaojoao();
saudacaoMaria();



