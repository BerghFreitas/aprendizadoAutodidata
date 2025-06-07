numero = 2

while numero < 5:
    if numero %2 == 0:
        print(f"{numero} é par")
        break
    else:
        print(f"{numero} é impar")
        break

contador = 0
while contador < 5:
    if contador % 2 == 0:
        print(f"{contador} é par")
    else:
        print(f"{contador} é ímpar")
    contador += 1