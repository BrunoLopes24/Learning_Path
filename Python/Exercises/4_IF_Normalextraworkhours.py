horas = float(input('Quantas horas faz?: '))
paga = float(input('Valor pago por hora: '))
if horas > 40:
    # print('Trabalhas a mais, o normal seria 35 horas por semana estás a fazer', horas - 35, 'a mais')
    reg = horas * paga
    pagamais = (horas - 40) * (paga * 0.5)  # Multiplica horas extras para determinar o bónus a mais que recebe
    # print(reg, pagamais)
    sal = reg + pagamais
else:
    # print('Trabalhas o normal')
    reg = horas * paga

print('O Salário é: ', sal)
