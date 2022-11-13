counts = dict()
line = input('Escreva uma frase: ')

palavras = line.split()  # Divide a frase por palavras

print('Palavras: ', palavras)
print('Contando...')

for palavra in palavras:
    counts[palavra.lower()] = counts.get(palavra, 0) + 1  # Conta as palavras e soma as repetidas
print('Contagem: ', counts)
