countries = ['Vietnam', 'Thailand', 'Australia', 'Germany', 'Great Britain', 'Belgium']
print(countries[3])
countries.insert(1,'Laos')
print(countries[3])
countries.pop()

country = input()
countries.insert(0, country)
print(countries)

animals = ['dog', 'platypus', 'duck', 'cat', 'bear', 'vodka']
countries = countries + animals
print(countries)