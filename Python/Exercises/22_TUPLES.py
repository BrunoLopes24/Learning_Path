# Tuples são outro tipo de sequências que têm muita semelhança com LISTS - Têm elementos que são indexados começando no 0
# Tuples = ()
# DICT = {}
# LISTS = []

x = ('Glen', 'Jones', 'Adam')
print(x[2])  # x = (0,1,2)
y = (1, 9, 2)
print(y)
print(max(y))  # Mostra o valor máx do TUPLE Y
print('---FOR---')
for iter in y:
    print(iter)

# Uma das diferenças entre TUPLE e LISTS é que o TUPLE, NÃO É, modificável/alterável.
print('----DIR----')
print(dir(x))  # Únicos métodos possíves são : .index | .count

# É possível colocar um TUPLE no lado esquerdo de uma instrução de atribuição
print('----Atribuições----')
(x, y) = (4, 'Bruno')
print('x =', x)
(a, b) = ('João', 'MARINHA')
print('b =', b)

# TUPLES é possivel comparar se é TRUE ou FALSE

comp = (0, 1, 2) < (5, 1, 2)  # Compara um a um do lado esquerdo para o direito|  0 < 5 = TRUE
print(comp)
comp1 = (0, 1, 200) < (0, 3, 4)  # Compara um a um do lado esquerdo para o direito|  0 < 0, 0 < 3 = TRUE
print(comp1)
comp2 = ('Jones', 'Sally') < ('Jones', 'Sam') # Compara um a um do lado esquerdo para o direito letra a letra no Abcedário
print(comp2)
comp3 = ('Jones', 'Sally') > ('Jones', 'Sally')
print(comp3)