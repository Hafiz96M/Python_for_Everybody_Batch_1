# List 
"""
A list is a collection of items in a specific order.
"""
persons = ['mehedi', 'robel', 'masum', 'sinkia']
print(persons)
print(persons[1])
# print(persons.title()[2]) # wrong
print(persons[2].title())
print(persons[-1])

persons.append('rupok')
print(persons)

persons.insert(1, 'ayakub')
print(persons)