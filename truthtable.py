import ttg

print('COMO USAR \n and = ^ \n or = v \n =>')

x1 = input('Digite aqui a primeira preposição: ')
x2 = input('Digite aqui a segunda preposição: ')
x3 = input('Digite aqui a terceira preposição: ')

table_val = ttg.Truths(['p', 'q', 'r'], [x1, x2, x3], ints=False)

print(table_val)

print('Essa tabela é uma ',table_val.valuation())