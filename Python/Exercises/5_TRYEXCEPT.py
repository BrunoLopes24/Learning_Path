horas = input('Quantas horas faz?: ')
paga = input('Valor pago por hora: ')
try:
     hora = float(horas)
     txpaga = float(paga)
except:
    print('Escreva um número numérico.')
    quit()

if hora > 40:
    reg = hora * txpaga
    pagamais = (hora - 40) * (txpaga * 0.5)  # Multiplica horas extras para determinar o bónus a mais que recebe
    sal = reg + pagamais
else:
    sal = hora * txpaga
print('O Salário é: ', sal)
