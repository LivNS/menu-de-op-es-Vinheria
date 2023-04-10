# RM 97819 


print("Bem-vindo(a) à Vinheira Agnello!!")
print("Para continuar realize um breve cadastro, por favor!!")

VALOR_MINIMO = 100.00
VALOR_FRETE = 25.00

nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
endereco = input("Digite seu endereço: ")
endereco_entrega = input("Digite o endereço de entrega: ")

# se o comprador for menor de idade sua compra será negada
if idade < 18:
    print("Desculpe, para continuar é necessário que você seja maior de idade.")
    
else:
    #catálogo de vinhos
    catalogo_vinhos = {
        "Fasano Brunello di Montalcino 2017": 899.00,
        "Casa Ferreirinha Vinha Grande Douro Tinto 2019": 189.90,
        "Vinho Canção Tinto Suave 750": 20.00,
        "Casa Santos Lima Confidencial Branco 2019": 90.00,
        "Premier Rendez-Vous Cinsault Rosé 2020": 109.00,
    }

    print("Veja as nossas opções de vinhos:")

    for vinho, preco in catalogo_vinhos.items():
        print(vinho, "- R$ {:.2f}".format(preco))


#quantidade
print("\n Digite a quantidade que deseja adicionar ao carrinho:")
compras = {}
quantidade_total = 0
for vinho in catalogo_vinhos.keys():
    compras[vinho] = {"quantidade": 0}

for vinho in catalogo_vinhos.keys():
    quantidade = int(input(vinho + ": "))
    compras[vinho]["quantidade"] = quantidade
    quantidade_total += quantidade

print("\n Resumo da sua compra:")
total = 0
for vinho, info in compras.items():
    quantidade = info["quantidade"]
    preco_unitario = catalogo_vinhos[vinho]
    preco_total = preco_unitario * quantidade
    total += preco_total
    print(vinho, "- {} unidades - R$ {:.2f}".format(quantidade, preco_total))

if total < VALOR_MINIMO:
    frete = VALOR_FRETE
    total += frete
    print("\n O valor do frete é de R$ {:.2f}.".format(frete))
elif total > 200.00:
    frete = 0.00
    print("\n Parabéns! Você ganhou frete grátis!!!")

#caso a compra seja menor que 200 reais o frete sera cobrado
if frete > 0:
    print("Valor do frete: R$ {:.2f}".format(frete))

print("\n Resumo final da compra:")
for vinho, info in compras.items():
    quantidade = info["quantidade"]
    preco_unitario = catalogo_vinhos[vinho]
    preco_total = preco_unitario * quantidade
    print(vinho, "- {} unidades - R$ {:.2f}".format(quantidade, preco_total))
print("Total da compra: R$ {:.2f}".format(total))

#mensagem de fim da compra
print("Você comprou {} produtos no valor total de R$ {:.2f}.".format(quantidade_total, total)) 
print("O endereço de entrega é: {}.".format(endereco_entrega))
print("\n Obrigado pela compra!")
