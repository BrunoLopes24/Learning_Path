counts = dict()
line = input('Escreva uma frase: ')

palavras = line.split()  # Divide a frase por palavras

print('Palavras: ', palavras)
plv = input('Qual a palavra quer contar? ')
print('Contando...')

for plv1 in palavras:
    counts[plv1.lower()] = counts.get(plv1.lower(), 0) + 1  # Conta as palavras e soma as repetidas

    if plv not in palavras:  # Se a palavra não estiver na lista, encerra o programa
        print('Não existe')
        quit()

print('A palavra', plv.lower(), 'aparece', counts[plv], 'vezes')
