def calculopagamento(horas, pagamento):
    # print('Em cálculo de pagamento:', horas, pagamento)
    if horas > 40:
        reg = horas * pagamento
        pagamais = (horas - 40) * (pagamento * 0.5)  # Multiplica horas extras para determinar o bónus a mais que recebe
        pg = reg + pagamais
    else:
        pg = horas * pagamento
    # print('Valor:', pg)
    return pg


horas = input('Quantas horas faz?: ')
paga = input('Valor pago por hora: ')
try:
    hora = float(horas)
    txpaga = float(paga)
except:
    print('Escreva um número numérico.')
    quit()

sal = calculopagamento(hora, txpaga)

print('O Salário é: ', sal)
