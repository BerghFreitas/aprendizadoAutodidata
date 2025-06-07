def somar(a, b):
    return a + b

def subtrair(a,b):
    return a - b

def calcular_numeros(a, b, funcao):
    calculo = funcao (a,b)
    if funcao == somar : print(f"a soma dos numeros {a} e {b} é {calculo}")
    else:
        print(f"a subtraçao dos numero {a} e {b} é {calculo}") 


calcular_numeros(12 ,23, subtrair)
