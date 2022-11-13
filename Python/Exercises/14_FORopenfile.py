fichname = open('txtexercicio_13.txt')
for line in fichname:
    line = line.rstrip()  # Remove espaçamentos entre linhas
    print(line.upper())
