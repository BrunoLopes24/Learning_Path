num = 0
total = 0.0

while True:
    sval = input('Escreva um número: ')  # SVAL = String value
    if sval == 'done':
        break
    try:
        fval = float(sval)  # Transforma um STR para FLOAT
    except:
        print('Algo errado')
        continue
    # print(fval)
    num = num + 1
    total = total + fval

print(num, total, total/num)
