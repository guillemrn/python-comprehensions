# Definición de un conjunto (set) llamado "set_countries" con tres elementos iniciales.
set_countries = {'col', 'mex', 'bol'}
print(set_countries)

# Obtiene el tamaño (número de elementos) del conjunto "set_countries" y lo imprime.
size = len(set_countries)
print(size)

# Verifica si 'col' y 'arg' están presentes en el conjunto "set_countries" e imprime el resultado.
print('col' in set_countries)
print('arg' in set_countries)

# Agrega el elemento 'arg' al conjunto "set_countries" y lo imprime.
set_countries.add('arg')
print(set_countries)

# Actualiza el conjunto "set_countries" agregando varios elementos.
set_countries.update({'pe', 'ecu', 'cl'})
print(set_countries)

# Elimina el elemento 'col' del conjunto "set_countries" utilizando el método "discard".
# set_countries.remove('col')
set_countries.discard('col')
print(set_countries)

# Limpia (borra todos los elementos) del conjunto "set_countries" y lo imprime, junto con su longitud actual (que será 0).
set_countries.clear()
print(set_countries, len(set_countries))
