idade = 25
tem_carteira = True
tem_carro = False

if idade >= 18:
    print("Maior de idade")
    
    if tem_carteira:
        print("Pode dirigir")
        
        if tem_carro:
            print("Tem um carro próprio")
        else:
            print("Pode dirigir, mas não tem carro próprio")
    else:
        print("Não pode dirigir, pois não tem carteira")
else:
    print("Menor de idade, não pode dirigir")


idade = 25
tem_carteira =  False
tem_carro = False

if idade < 18:
    print("Menor de idade, não pode dirigir")
elif not tem_carteira:
    print("Não pode dirigir, pois não tem carteira")
elif tem_carro:
    print("Pode dirigir e tem um carro próprio")
else:
    print("Pode dirigir, mas não tem carro próprio")

