# VERIFICA SE EXISTE ALGO NA LISTA
print('VERIFICA SE EXISTE ALGO NA LISTA')
some = [1, 9, 33, 23, 21]
print(1 in some)
print(3 in some)

some.sort()  # Ordena de forma crescente
print(some)

# CRIA LISTA VAZIA
print('CRIA LISTA VAZIA')
stuff = list()  # Cria uma lista vazia
print(stuff)
stuff.append('Book')  # Adiciona 'Book' à lista
stuff.append(99)  # Adiciona 99 à lista
print(stuff)
stuff.append('cookie')  # Adiciona 'cookie' à lista
print(stuff)

# DIVIDIR A LISTA
print('DIVIDIR A LISTA')
t = [1, 4, 22, 11, 53, 99, 199]

print(t[1:3])  # Mostra o 2º e 3º valor da lista
print(t[:4])  # Mostra até ao 3º valor da lista
print(t[3:])  # Começa no 3º valor da lista
print(t[:])  # Mostra todos os valores da lista

print(type(t))  # Mostra o tipo de variável
print(dir(t))  # Mostra o tipo de métodos possíveis para a variável

# MOSTRA POR LINHAS UMA LISTA USANDO FOR
print('MOSTRA POR LINHAS UMA LISTA USANDO FOR')
friends = ['Bruno', 'Joana', 'Bruna']  # Uma variável com uma lista de nomes
for friend in friends:
    print('Bem vindo(a)', friend, '!')

print('Done')

# MÉDIA DE VÁRIOS NUM EM LISTAS (LOOP EM LISTA)
print('MÉDIA DE VÁRIOS NUM EM LISTAS')

numlist = list()
while True:
    num = input('Escreva um numero (done para terminar):')
    if num == 'done':
        break
    value = float(num)  # Converte string em float no valor escrito anteriormente
    numlist.append(value)  # Adiciona os valores escritos na lista
media = sum(numlist)/len(numlist)  # Soma a lista e divide pelo total de valores escritos na lista [3, 9, 5] | 3+9+5/3
print('A média é:', media)