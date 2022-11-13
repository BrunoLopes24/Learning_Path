counts = dict()
names = ["Bruno", "Lena", "Lena", "Jose", "Joao", "Adriana", 'Bruno']  # Uso do DICT com {}

for name in names:
    # Forma simplificada
    counts[name] = counts.get(name, 0) + 1  # No dict 'name', irá buscar 'get' o 'name' se não houver não adiciona '0', se houver '+1'
    # Forma não simplificada:
    #if name not in counts:
    #    counts[name] = 1  # Se o nome não estiver no dict, adiciona como novo.
    #else:
    #    counts[name] = counts[name] + 1   # Se o nome estiver no dict soma.
print(counts)
