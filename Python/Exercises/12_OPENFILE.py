fname = input('Qual o nome do do ficheiro que quer abir?: ')
fhand = open(fname)  # vai abrir o respectivo ficheiro
count = 0
for line in fhand:
    if line.startswith('Subject:'):  # ver as linhas que começam com 'Subject' e contar
        count = count + 1
print('Contagem de:', count, 'subject linhas no', fname)  # Mostra o somatório da contagem anterior feita no ficheiro