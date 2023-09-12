set_countries = {'col', 'mex', 'bol'}
print(set_countries)


size = len(set_countries)
print(size)

print('col' in set_countries)
print('arg' in set_countries)

# Add
set_countries.add('arg')
print(set_countries)

# Update
set_countries.update({'pe', 'ecu', 'cl'})
print(set_countries)

# Remove
# set_countries.remove('col')
set_countries.discard('col')
print(set_countries)

set_countries.clear()
print(set_countries, len(set_countries))