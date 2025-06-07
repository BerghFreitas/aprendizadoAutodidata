numeros = [2,3,4,5,6,7,8,9,34,56,87,23,45,664,24,46,35,46,68]
pares = [numero for numero in numeros if numero % 2 == 0 ] #maneira mais facil de fazer uma selecao de uma lista
print(pares) 

quadrado = [numero ** 2 for numero in numeros]
print(quadrado) 