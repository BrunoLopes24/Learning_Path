import re

x = 'My 2 favorites numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

s = 'From brunolopes148@gmail.com Sab 14 jun 2022'
b = re.findall('^From (\S+@\S+)', s)  # Mostra os non-space antes e depois do @
print(b)

# Extrair parte de uma string

lin = 'From brunolopes148@gmail.com Sab 14 jun 2022'
ext = re.findall('@([^ ]*)', lin)
print(ext)
