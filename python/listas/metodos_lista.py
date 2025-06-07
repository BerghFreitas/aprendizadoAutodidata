#. Adicionando Elementos
"""
✅ append(item) – Adiciona um item no final da lista.
✅ insert(índice, item) – Insere um item em uma posição específica.
numeros.append(50)  
print(numeros)  # [10, 20, 30, 40, 50]

numeros.insert(2, 25)  
print(numeros)  # [10, 20, 25, 30, 40, 50]

"""
#Removendo Elementos
"""
✅remove(valor) – Remove a primeira ocorrência de um valor.
✅ pop(índice) – Remove e retorna o elemento de um índice.
✅ clear() – Remove todos os elementos da lista.

numeros.remove(30)
print(numeros)  # [10, 20, 25, 40, 50]

removido = numeros.pop(1)
print(removido)  # 20
print(numeros)   # [10, 25, 40, 50]

numeros.clear()
print(numeros)  # []

"""
#Ordenação e Reverso
"""
✅ sort() – Ordena a lista (crescente por padrão).
✅ sort(reverse=True) – Ordena de forma decrescente.
✅ reverse() – Inverte a ordem dos elementos.

numeros = [40, 10, 30, 20, 50]

numeros.sort()
print(numeros)  # [10, 20, 30, 40, 50]

numeros.sort(reverse=True)
print(numeros)  # [50, 40, 30, 20, 10]

numeros.reverse()
print(numeros)  # [10, 20, 30, 40, 50] (inverte sem ordenar)
"""
#Copiando e Contando Elementos
"""
✅ count(valor) – Conta quantas vezes um valor aparece na lista.
✅ copy() – Cria uma cópia da lista.

numeros = [10, 20, 30, 10, 40, 10]
print(numeros.count(10))  # 3

copia = numeros.copy()
print(copia)  # [10, 20, 30, 10, 40, 10]
"""

#Concatenando e Expandindo Listas
"""
✅ extend(lista2) – Adiciona os elementos de outra lista.
✅ + – Também pode ser usado para concatenar listas.

a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]

c = a + b
print(c)  # [1, 2, 3, 4, 5, 6, 4, 5, 6]
"""