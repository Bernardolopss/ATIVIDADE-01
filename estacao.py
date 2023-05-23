m = int(input("digite um número do mês (entre 1 e 12): "))

if m in [1,2,3]:
    est = "Verão"
elif m in [4,5,6]:
    est = "Outono"
elif m in [7,8,9]:
    est = "Inverno"
elif m in [10,11,12]:
    est = "Primavera"
else:
    est = "erro: numero invalido, tente novamente"

print("a estação do ano do mês", m, "é", est)
