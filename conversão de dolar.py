print('PROGRAMA DESENVOLVIDO PARA CONVERSÃO DE DOLÁR PARA REAIS')
dolar = float(input('Digite a quantidade que deseja converter($):'))

conversao = dolar * 5.01

print('o seu valor em reais será: R$', conversao)

euroo = (input(' deseja saber em euros?: '))
if euroo == "sim":
    
    qtdeuro = float(input('Digite a quantidade que deseja converter: £'))
    
    euro_real = qtdeuro * 5.49
    print('Você tem : R$', euro_real)
    
elif euroo == "não":
    print('okay')
