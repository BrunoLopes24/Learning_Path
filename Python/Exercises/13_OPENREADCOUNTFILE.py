+fname = input('Qual o nome do do ficheiro que quer abir?: ')
try:
    fhand = open(fname)  # vai abrir o respectivo ficheiro
except:
    print('Ficheiro não pode ser aberto.', fname.upper())  # Erro na abertura do ficheiro e mostra em maiuscula o nome
    quit()

# Caso exista o ficheiro, o programa continua:
count = 0
for line in fhand:
    if line.startswith('Subject:'):  # ver as linhas que começam com 'Subject' e contar
        count = count + 1
print('Contagem de:', count, 'subject linhas no', fname)  # Mostra o somatório da contagem anterior feita no ficheiro