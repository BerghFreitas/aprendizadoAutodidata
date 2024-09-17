/* aqui é um modelo callback feito sem olhar*/


/*function saudacao (nome, callback){
    console.log('ola ' + nome);
    callback(); 

}
function despedida (){
    console.log('ate logo');
}
saudacao('berg', despedida);*/

function saudacao (nome, callback){
    console.log('ola ' + nome);
    callback();
}
function boasVindas(){
    console.log('seja bem vindo')
}

saudacao('bergh', boasVindas)