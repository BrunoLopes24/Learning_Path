# NON RESOLVED!!!!!
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')  # Mostra qual a Database (DB)
cur = conn.cursor()  # Conecta à DB

cur.execute('''
DROP TABLE IF EXISTS Counts''')  # Elimina (DROP) TABLE se existir Counts

cur.execute('''
Create TABLE Counts (email TEXT, count INTEGER)''')  # Cria a TABLE Counts com email e count

fname = input('Enter file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'  # Se o ficheiro tiver menos de 1 de comprimento de caracter
fh = open(fname, encoding='')
for line in fh:  # Para cada linha no fh
    if not str(line).startswith('From: '):
        continue  # Se NÃO começar com 'From: ' continua
    pieces = line.split()  # Divide as palavras em divisórias  '0|1|2'
    email = pieces[1]  # Email na divisão 1
    cur.execute('SELECT count FROM Counts WHERE email = ?',
                (email,))  # Executa a selecção 'count' de 'Counts' onde 'email = ?'
    row = cur.fetchone()  # Mostra o valor escrito na linha acima
    if row is None:  # Se row estiver vazio
        cur.execute('''INSERT INTO Counts (email,count)
                VALUES (?,1)''', (
            email,))  # Insere no Counts os valores (email,count) =(? -> o que está escrito no ficheiro, 1 -> Divisória 1)
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ? ',
                    (email,))  # Faz a contagem de email onde email = ?
    conn.commit()  # Garante que as mudanças foram bem consistentes

sqlstr = 'SELECT email count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])  # row[0] -> email | row[1] -> count

cur.close()
