nota = float(input("Digite a nota do aluno: "))
if nota == 10:
    media = "Excelente"
elif nota >= 8:
     media = "Ótimo"
elif nota >= 7:
     media = "Bom"
elif nota >= 5:
    media = "Regular"
else:
     media = "Insuficiente"