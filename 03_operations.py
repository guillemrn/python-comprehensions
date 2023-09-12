# Definición de dos conjuntos (set) llamados "set_a" y "set_b" con elementos iniciales.
set_a = {'col', 'mex', 'bol'}
set_b = {'arg', 'bol'}

# Unión de los conjuntos "set_a" y "set_b" y luego se imprime el resultado.
set_c = set_a.union(set_b)
print(set_c)
# Otra forma de realizar la unión de los conjuntos "set_a" y "set_b" utilizando el operador "|" y se imprime el resultado.
print(set_a | set_b)

# Intersección de los conjuntos "set_a" y "set_b" y luego se imprime el resultado.
set_c = set_a.intersection(set_b)
print(set_c)
# Otra forma de realizar la intersección de los conjuntos "set_a" y "set_b" utilizando el operador "&" y se imprime el resultado.
print(set_a & set_b)

# Diferencia entre los conjuntos "set_a" y "set_b" (elementos en "set_a" pero no en "set_b") y luego se imprime el resultado.
set_c = set_a.difference(set_b)
print(set_c)
# Otra forma de calcular la diferencia entre los conjuntos "set_a" y "set_b" utilizando el operador "-" y se imprime el resultado.
print(set_a - set_b)

# Diferencia simétrica entre los conjuntos "set_a" y "set_b" (elementos que están en uno de los conjuntos pero no en ambos) y luego se imprime el resultado.
set_c = set_a.symmetric_difference(set_b)
print(set_c)
# Otra forma de calcular la diferencia simétrica entre los conjuntos "set_a" y "set_b" utilizando el operador "^" y se imprime el resultado.
print(set_a ^ set_b)
