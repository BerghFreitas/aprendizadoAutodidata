
function contador() {
    let count = 0;
    return function() {
        count++;
        return count;
    };
}

const incrementar = contador();
console.log(incrementar()); // Saída: 1
console.log(incrementar()); // Saída: 2
console.log(incrementar());