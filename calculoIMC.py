peso = float(input("digite seu peso(kg): "))

altura = float(input("Digite a sua altura(m): "))

imc = peso / altura ** 2

if imc < 18.5:
    diag = "baixo peso"
elif imc < 25:
    diag = "normal"
elif imc < 30:
    diag = "sobrepeso"
elif imc < 35:
    diag = "obesidade classe I"
elif imc < 40:
    diag = "obesidade classe II"
else:
    diag = "obesidade classe III"

print("Seu IMC é:", imc)

print("avaliação:", diag)
