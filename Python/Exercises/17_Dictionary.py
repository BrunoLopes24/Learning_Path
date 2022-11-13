purse = dict()  # Cria um dicionário vazio
purse['Money'] = 12  # Insere Money na 'Purse'
purse['Candy'] = 3  # Insere Candy na 'Purse'
purse['Tissues'] = 75  # Insere Tissues na 'Purse'
print(purse)
print(purse['Candy'])  # Mostra o valor da 'Candy'
purse['Candy'] = purse['Candy'] + 2   # Adiciona 2 ao valor da 'Candy'
print(purse)
print('----SORT')
# Sort DICT
d = {'a': 2, 'c': 1, 'b': 200}
print(d.items())
print(sorted(d.items()))  # Mete por ordem de Letra ignorando os valores.
