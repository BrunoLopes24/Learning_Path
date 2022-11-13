name = input('Qual o ficheiro que quer abrir? ')
handle = open(name)  # Abre ficheiro escolhido
# ---

counts = dict()  # Cria um DICT
for line in handle:
    words = line.split()  # Divide cada palavra da frase
    for word in words:
        counts[word] = counts.get(word, 0) + 1  # Conta as palavras e SOMA

# ---

bigcount = None  # Variável para o número da palavra mais repetida
bigword = None  # Variável para a palavra mais repetida
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print('Palavra mais repetida: ', bigword, 'número de vezes: ', bigcount)
