word = 'His e-mail is q-lar@freecodecamp.org'
pieces = word.split()  #Divide o texto(string) em uma lista = ['His', 'e-mail', 'is', 'q-lar@freecodecamp.org']
print(pieces)
parts = pieces[3].split('-')  #No mail divide no ('-') = ['q', 'lar@freecodecamp.org']
print(parts)
n = parts[1]
print(n)
