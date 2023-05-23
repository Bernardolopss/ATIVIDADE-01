cod = int(input("digite o código: "))

qtd = int(input("digite a quantidade que irá querer: "))

if cod == 100:
    preco = 1.20
    desc = "Cachorro-quente"
elif cod == 101:
    preco = 1.30
    desc = "Bauru"
elif cod == 102:
    preco = 1.20
    desc = "Hambúrguer"
elif cod == 103:
    preco = 1.30
    desc = "Cheeseburguer"
elif cod == 104:
    preco = 1.00
    desc = "Refrigerante"

else:
    print("erro no código")
    preco = 0
    desc = ""

total = preco * qtd

if desc != "":
    print(f"Você pediu {qtd} {desc}(s), que custam {preco:.2f} cada um. Isso tudo custa: {total:.2f}")