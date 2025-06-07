

endereco = {"rua": "norma guilhon", "numero": "100"}
dados_pessoais = {"nome":"aldembergue", "idade": "30"}

pessoas = {
    "pessoa1":
    {"nome": "aldembergue", "idade":"28",
    "endereco": "sao paulo"},
    
    "pessoa2":
    {"nome": "pedro", "idade":"30",
    "endereco":"fortaleza"}

}
pessoas["pessoa2"]["nome"]= "francisco"
print(pessoas["pessoa2"]["nome"])
"""
endereco ["complemento"] ="bloco 5 ap 301" #adciona o valor complemento dentro da chave endereco
endereco ["complemento"] = "bloco 6 ap 401" #sobrescreveu o valor antigo

print(endereco)
print(dados_pessoais)
"""
"""for chave in pessoas:
    print(chave, pessoas[chave])"""
"""for chave, valor in pessoas.items():
    print(f"A chave é {chave} e o valor é {valor}")"""

""".items() retorna dois argumentos o primeiro é a chave e o segundo é o valor,
no caso exemplo acima chave e valor respectivamente - for chave, valor"""